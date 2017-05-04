from dresponse.handler import BaseDresponseHandler


class MyHandler(BaseDresponseHandler):
    def handle(self, root, netns, container_attrs, image_attrs):
        name = container_attrs['Name']
        labels = container_attrs['Config']['Labels']
        print 'there are %d labels for container %s:' % (len(labels), name)
        print '\n'.join(labels.keys())
