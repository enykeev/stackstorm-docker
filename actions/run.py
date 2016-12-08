from lib.base import DockerBasePythonAction


__all__ = [
    'DockerRunAction'
]


class DockerRunAction(DockerBasePythonAction):
    def run(self, *args, **kwargs):
        container = self.client.create_container(*args, **kwargs)
        self.client.start(container=container.get('Id'))

        if kwargs.get('detach'):
            return container

        self.client.wait(container=container.get('Id'))
        return self.client.logs(container=container.get('Id'))
