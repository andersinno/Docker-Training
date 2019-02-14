# Building with Docker Compose

## Objective

* Create a Dockerfile that runs the python script `main.py`
* Create a Docker Compose configuration that builds and runs the Dockerfile
* Run and verify it works
* Make modifications to `main.py`
* Re-run (and build) and verify the changes were applied

## Pointers

* Documentation: [https://docs.docker.com/compose/compose-file/](https://docs.docker.com/compose/compose-file/)
    * `docker-compose up` will start the containers defined in `docker-compose.yml`
        * Passing the `--build` flag will make compose re-build all the containers on launch.
    * `docker-compose down` will stop the containers defined in `docker-compose.yml`
    * Short template docker-compose.yml:
    ```yml
    version: '3'

    services:
      # This is what the container will be called
      SERVICE_NAME_HERE:
        image: IMAGE_NAME_HERE
        # Add other parameters as needed
    
      # Add other services as needed
    ```
    * Use the `build` configuration to point a service to a local Dockerfile instead of an image
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

## Up next

[31 - Containerizing a RealWorld ExampleApp](../31-RealWorldExample/README.md)
