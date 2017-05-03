import os
import logging
import subprocess
import importlib


LOG = logging.getLogger(__name__)


class BaseDresponseHandler(object):
    def __init__(self, flask_app):
        self.app = flask_app

    def handle(self, root, netns, container_attrs, image_attrs):
        pass


class DummyHandler(BaseDresponseHandler):
    pass


class RunScriptsHandler(BaseDresponseHandler):
    DEFAULT_DRESPONSE_SCRIPTS_DIR = '/var/lib/docker-wait/prestart'

    def handle(self, root, netns, container_attrs, image_attrs):
        scripts = self.collect_scripts()
        env = self.compose_env(root, netns, container_attrs, image_attrs)

        for script in scripts:
            self.execute(script, env)

    def collect_scripts(self):
        directory = self.app.config.get('DRESPONSE_SCRIPTS_DIR',
                                        self.DEFAULT_DRESPONSE_SCRIPTS_DIR)
        scripts = []
        if not os.path.exists(directory):
            LOG.warn('%s not existed!', drectory)
            return scripts

        if not os.path.isdir(directory):
            LOG.warn('%s not a directory!', directory)
            return scripts

        for f in os.listdir(directory):
            abs_file_name = os.path.join(directory, f)
            if os.path.isfile(abs_file_name) and\
               os.access(abs_file_name, os.X_OK):
                scripts.append(abs_file_name)

        scripts.sort()
        return scripts


    def compose_env(self, root, netns, container_attrs, image_attrs):
        env = {
            'CONTAINER_ROOT_FS': root,
            'CONTAINER_NET_NS': netns
        }

        env['CONTAINER_HOSTNAME'] = container_attrs['Config']['Hostname']

        for key, value in container_attrs['Config']['Labels'].iteritems():
            key = key.upper().replace('.', '_')
            env['CONTAINER_LABEL_%s' % key] = str(value)

        env['IMAGE_NAME'] = container_attrs['Config']['Image']
        env['IMAGE_AUTHOR'] = image_attrs['Author']
        return env


    def execute(self, script, env):
        return subprocess.check_call(script, env=env)


def get_handlers(flask_app):
    handlers = []
    specified = flask_app.config.get('DRESPONSE_HANDLERS',
                                     [
                                      'dresponse.handler:DummyHandler',
                                      'dresponse.handler:RunScriptsHandler',
                                     ])

    for string in specified:
        module_name, class_name = string.split(':')
        module = importlib.import_module(module)
        cls = getattr(module_name, class_name)
        handlers.append(cls(flask_app))

    return handlers
