from lib.base import DockerBasePythonAction


__all__ = [
    'DockerRmAction'
]


class DockerRmAction(DockerBasePythonAction):
    def run(self, *args, **kwargs):
        remove_volumes = kwargs.pop('remove_volumes')
        return self.client.remove_container(*args, v=remove_volumes, **kwargs)
