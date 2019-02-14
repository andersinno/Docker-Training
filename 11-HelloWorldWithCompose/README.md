# Hello World With Compose

## Objective

* Use docker-compose to run the Hello World container

## Pointers

* Documentation: [https://docs.docker.com/compose/compose-file/](https://docs.docker.com/compose/compose-file/)
* `docker-compose up` will start the containers defined in `docker-compose.yml`
    * Passing the `-d` flag will cause the containers to be ran on the background
* `docker-compose down` will stop the containers defined in `docker-compose.yml`
* Short template docker-compose.yml
    ```yml
    version: '3'

    services:
      # This is what the container will be called
      SERVICE_NAME_HERE:
        image: IMAGE_NAME_HERE
        # Add other parameters as needed
    
      # Add other services as needed
    ```

## Up next

[12 - Nginx and Volumes](../12-NginxAndVolumes/README.md)
