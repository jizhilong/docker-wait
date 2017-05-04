# docker-wait
[![Build Status](https://travis-ci.org/jizhilong/docker-wait.svg?branch=master)](https://travis-ci.org/jizhilong/docker-wait)
[![Docker Pulls](https://img.shields.io/docker/pulls/jizhilong/docker-wait.svg)]()

`docker-wait` is a pre-startup hook for docker containers

## what can you do with docker-wait?
### run arbitary scripts before containers start.
Within the scripts, these container attributes are provided via environment variables:

1. container's hostname, labels, image name, image.
2. path to container's root filesystem.
3. container's network namespace which you can access by `ip netns exec $CONTAINER_NET_NS <cmd>`.

You can do whatever needed to init or validate a container's runtime environment before its entrypoint/command starts,
include but not limited to:

1. validate the checksum of a specific path inside the container.(see [example](examples/validate-checksum-of-bash))
2. add some iptables rule to the container's network namespace.
3. decrept secret data inside the container with a private key installed on the host.

### run some python code snnipet before containers start.
see [example](examples/customize-python-handler).

## how does docker-wait work?
1. specify container' entrypoint to a customized golang program named dwait via `docker run -v /usr/lib/dwait:/d -v /var/run/dwait/:/.dwait --entrypoint /d/dwait`.
2. dwait POST a HTTP request over unix socket to dresponse-a service running on the host.
3. dresponse execute all prestart hooks for the container and return the container's command and image entrypoint via HTTP response.
4. dwait read and parse the actual entrypoint and command from the HTTP response body, and launch them with a `exec` system call.
