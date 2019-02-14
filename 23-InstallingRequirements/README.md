# Installing Requirements

## Objective

* Build a container image that runs the `main.py` script by default when launched.
* Install the requirements when building the container.
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
* Use a python image as the base.
* Use the `RUN` command to execute commands in the container when building it.

## Up next

[24 - Building with Docker Compose](../24-BuildingWithDockerCompose/README.md)
