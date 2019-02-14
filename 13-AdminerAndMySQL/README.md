# Adminer and MySQL

## Objective

* Use docker-compose to run Adminer and MySQL together

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
* Use the `depends_on` configuration to link the containers to the same network
    * Network name alias will be the same as the container's service name
* Use the `environment` configuration to define required environment variables
* Make sure to use the correct version of MySQL, as Adminer won't work with MySQL > 5.7

## Up next

[14 - Redmine with Persistent Storage](../14-RedmineWithPersistentStorage/README.md)
