# Nginx and Volumes

## Objective

* Use docker-compose to run nginx with a volume mount
* Get nginx to display the "Hello, Aslan!" message

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
* Use the `ports` configuration to expose the nginx to the host network
* Use the `volumes` configuration to map a directory from the host to the container
  * Mount the `html` directory to the correct location
  * Use the `nginx` images [dockerhub page](https://hub.docker.com/_/nginx) as a reference

## Up next

[13 - Adminer and MySQL](../13-AdminerAndMySQL/README.md)
