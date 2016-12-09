from lib.base import DockerBasePythonAction


__all__ = [
    'DockerExecAction'
]


class DockerExecAction(DockerBasePythonAction):
    def run(self, *args, **kwargs):
        detach = kwargs.pop('detach')
        execution = self.client.exec_create(*args, **kwargs)
        return self.client.exec_start(exec_id=execution.get('Id'), detach=detach)
