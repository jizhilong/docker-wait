class BaseDresponseHandler(object):
    def handle(self, root, netns, container_attrs, image_attrs):
        pass


class DummyHandler(BaseDresponseHandler):
    pass


class RunExecutablesHandler(BaseDresponseHandler):
    EXECUTABLES_DIR = '/var/lib/dresponse/pre_start'

    def handle(self, root, netns, container_attrs, image_attrs):
        pass

    def compose_env(self, container_attrs, image_attrs):
        pass

    def execute(self, fname, env):
        pass


def get_handlers():
    return [DummyHandler(),
            RunExecutablesHandler()]
