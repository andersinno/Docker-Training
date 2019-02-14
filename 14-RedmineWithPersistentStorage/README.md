# Redmine with Persistent Storage

## Objective

* Use docker-compose to run Redmine with persistent storage
* Use a named volume for the storage

## Bonus

* Use a database server rather than Redmine's default sqlite
* Add adminer to the configuration so the database can be inspected

## Pointers

* Documentation: [https://docs.docker.com/compose/compose-file/](https://docs.docker.com/compose/compose-file/)
* `docker-compose up` will start the containers defined in `docker-compose.yml`
    * Passing the `-d` flag will cause the containers to be ran on the background
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
* Use named volumes for implementing persistent storage
* Look for help on how to use the images from their dockerhub page

## Up next

[21 - Building a Hello World Container](../21-BuildingHelloWorldContainer/README.md)
