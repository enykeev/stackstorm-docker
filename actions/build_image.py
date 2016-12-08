import os
import sys

try:
    import simplejson as json
except:
    import json

import six

from lib.base import DockerBasePythonAction


__all__ = [
    'DockerBuildImageAction'
]


class DockerBuildImageAction(DockerBasePythonAction):
    def _build(self, path=None, fileobj=None, tag=None):
        if path is None and fileobj is None:
            raise Exception('Either dir containing dockerfile or path to dockerfile ' +
                            ' must be provided.')
        if path is not None and fileobj is not None:
            sys.stdout.write('Using path to dockerfile: %s\n' % fileobj)
        opts = self._docker_build_opts
        sys.stdout.write('Building docker container. Path = %s, Tag = %s\n' % (path, tag))
        # Depending on docker version, stream may or may not be forced. So let's just always
        # use streaming.
        result = self.client.build(path=path, fileobj=fileobj, tag=tag, quiet=opts['quiet'],
                                    nocache=opts['nocache'], rm=opts['rm'],
                                    stream=True, timeout=opts['timeout'])
        try:
            json_output = six.advance_iterator(result)
            while json_output:
                output = json.loads(json_output)
                sys.stdout.write(output['stream'] + '\n')
                json_output = six.advance_iterator(result)
        except StopIteration:
            pass
        except Exception as e:
            sys.stderr.write('Error: %s' % (str(e)))
            raise e

    def run(self, dockerfile_path, tag):
        if os.path.isdir(dockerfile_path):
            return self._build(path=dockerfile_path, tag=tag)
        else:
            dockerfile_path = os.path.expanduser(dockerfile_path)
            with open(dockerfile_path, 'r') as fp:
                return self._build(fileobj=fp, tag=tag)
