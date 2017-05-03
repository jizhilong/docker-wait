import json
import logging
import hashlib
import errno
import os

import flask
import docker

from dresponse import handler


LOG = logging.getLogger('dresponse')


def is_running_in_container():
    return os.environ.get('INCONTAINER', '0') == '1'


def get_app():
    app = flask.Flask('dresponse', instance_path='/etc/docker_wait',
                      instance_relative_config=True)
    app.config.from_pyfile('dresponse.cfg', silent=True)
    app.docker = docker.from_env()
    app.handlers = handler.get_handlers(app)
    app.in_container = is_running_in_container()
    if app.in_container:
        app.hostroot = '/hostroot'
    else:
        app.hostroot = '/'
    return app


app = get_app()


def calculate_auth_token(container_id):
    hasher = hashlib.sha256(container_id+app.secret_key)
    return hasher.hexdigest()


def verify_auth_token(container_id, token):
    if calculate_auth_token(container_id) != token:
        flask.abort(401)


def make_netns_symlink(pid, name):
    netns_dir = '/var/run/netns'
    if not os.path.exists(netns_dir):
        os.makedirs(netns_dir, mode=0755)
    source = os.path.join(app.hostroot, 'proc', str(pid), 'ns', 'net')
    dest = os.path.join(netns_dir, name)
    os.symlink(source, dest)


def destroy_netns_symlink(name):
    try:
        os.remove(os.path.join('/var/run/netns', name))
    except OSError as err:
        if err.errno == errno.ENOENT:
            pass
        else:
            raise err


@app.route("/init", methods=['POST'])
def init():
    json_data = flask.request.get_json(force=True)

    container_id = json_data['container_id']
    container = app.docker.containers.get(container_id)

    image = app.docker.images.get(container.attrs['Config']['Image'])
    entrypoint = image.attrs['Config']['Entrypoint'] or []
    command = container.attrs['Config']['Cmd'] or image.attrs['Config']['Cmd']

    pid = container.attrs['State']['Pid']
    root = os.path.join(app.hostroot, 'proc', str(pid), 'root')
    make_netns_symlink(pid, container.id)

    try:
        for handler in app.handlers:
                handler.handle(root, container.id,
                               container.attrs,
                               image.attrs)
    except Exception as e:
        LOG.exception('failed to run handler')
        raise e
    finally:
        destroy_netns_symlink(container.id)

    return flask.jsonify({'entrypoint': entrypoint, 'command': command,
                          'token': calculate_auth_token(container_id)})


@app.route("/reboot", methods=['POST'])
def reboot():
    json_data = flask.request.get_json(force=True)

    container_id = json_data['container_id']
    verify_auth_token(container_id, flask.request.headers.get('Auth-Token'))
    container = app.docker.containers.get(container_id)
    container.restart()
    return flask.jsonify({'rebooted': container_id})
