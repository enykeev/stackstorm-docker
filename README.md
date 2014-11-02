# Docker integration

This package contains some sample docker integrations.

## Actions

### Build docker image

This action builds a docker image given a path to Dockerfile (could be
directory containing Dockerfile or path to Dockerfile or remote URL containing
Dockerfile) and a tag to use for the image.

## Sensors

### Docker container spun up/shut down

This sensor watches the list of containers on local box and sends triggers
whenever a new container is spun up or an exisiting one is shut down.

## Requirements

1. Python 2.7 or greater
2. docker-io (version 1.13 or later)
3. pip install docker-py (0.4.0 or later)

YMMV if you use versions not listed here.

## Configuration

1. Edit config.yaml and look at the options. These options mirror the options of docker CLI.

## Notes

If you are connecting to the Docker daemon via the Unix socket, you need to
make sure that this socket is accessible to the system user under which
StackStorm processes are running.
