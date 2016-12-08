from lib.base import DockerBasePythonAction


__all__ = [
    'DockerPullImageAction'
]


class DockerPullImageAction(DockerBasePythonAction):
    def run(self, repo, tag=None, all_tags=None, insecure_registry=False,
            auth_username_override=None, auth_password_override=None):

        if all_tags:
            tag = None

        if auth_username_override and auth_password_override:
            auth_config = {
                'username': auth_username_override,
                'password': auth_password_override
            }
            return self.call('pull', repo, tag=tag, insecure_registry=insecure_registry,
                             auth_config=auth_config)
        else:
            return self.call('pull', repo, tag=tag, insecure_registry=insecure_registry)
