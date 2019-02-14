# Building a Hello World Container Image

## Objective

* Create a Dockerfile that builds into a container image that outputs `Hello World`.
* Run the container and verify it works.

## Pointers

* Documentation: [https://docs.docker.com/engine/reference/builder/](https://docs.docker.com/engine/reference/builder/)
* `docker build .`  will build the Dockerfile in the current directory
  * The `.` indicates that the Dockerfile's build context is this directory, and can not access any parent directories.
  * The `-f NAME` parameter can be used to define what file to build. By default, a file called `Dockerfile` is being looked for.
  * Use `-t NAME` to tag the built image with a name. This way that name can be used to later on run the container image.
* Short template Dockerfile:
    ```Dockerfile
    FROM ubuntu

    ENTRYPOINT ["/bin/echo", "Hello"]
    CMD ["World"]
    ```
* The `FROM IMAGENAME:VERSION` defines what to use as the base image for the container image. Any changes on top of that will be additional changes to the base image.
* The `ENTRYPOINT` defines what executable (and parameters) the container will launch with when ran.
* The `CMD` defines the default command to run. The CMD parameter contents will be passed/suffixed to the entrypoint, so the example here becomes `/bin/echo Hello World`.
  * It is possible to easily override the default command when running containers. For example, if this container were to be built and ran, we could override the CMD by doing `docker run <image> Aslan`. This would then replace the CMD with `Aslan` instead of `World`, and the complete command would result in `/bin/echo Hello Aslan`.

## Up next

[22 - Python Script Container](../22-PythonScriptcontainer/README.md)
