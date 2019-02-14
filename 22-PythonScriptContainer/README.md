# Building a Python Script Container

## Objective

* Build a container image that runs the `hello.py` script by default when launched.
* Also include the `world.py` script in the container and make it possible to be ran by changing the CMD.
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
* Use a python image as the base
* Use the `WORKDIR` command to specify the working directory within the container
* Use the `COPY` comand to include files to the container

## Up next

[23 - Installing Requirements](../23-InstallingRequirements/README.md)
