import sys

import docker

from st2actions.runners.pythonrunner import Action

__all__ = [
    'DockerBasePythonAction'
]


class DockerBasePythonAction(Action):
    def __init__(self, config):
        super(DockerBasePythonAction, self).__init__(config=config)

        # Assign sane defaults.
        if self.config['version'] is None:
            self.config['version'] = '1.24'
        if self.config['url'] is None:
            self.config['url'] = 'unix://var/run/docker.sock'

        self._version = self.config['version']
        self._url = self.config['url']
        self._timeout = 10
        if self.config['timeout'] is not None:
            self._timeout = self.config['timeout']

        self.client = docker.Client(base_url=self._url,
                                    version=self._version,
                                    timeout=self._timeout)
        self._docker_build_opts = self.config['build_options']

    def call(self, method, *args, **kwargs):
        try:
            method = getattr(self.client, method)
            for line in method(*args, **kwargs):
                sys.stdout.write(line)
        except Exception as e:
            sys.stderr.write('Error: %s' % (str(e)))
            raise e
