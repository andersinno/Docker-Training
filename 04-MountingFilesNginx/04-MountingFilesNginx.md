# Mounting files to Nginx

## Objective

* Run a docker container based on the `nginx` container image.
* Expose the Nginx port from the container to the host.
* Make the Nginx container serve custom HTML by mounting files inside the container.
* Use the `docker stop` command to stop the nginx container.

## To-do

* CD into this folder on your terminal (or substitute the paths in the next command accordingly).
* Run `docker run --rm --name nginx -v $(PWD)/html:/usr/share/nginx/html:ro -d -p 8080:80 nginx` on your terminal.
    * The `-v HOSTPATH:CONTAINERPATH:OPTIONS` option will mount the directory on the host at `HOSTPATH` inside the container at `CONTAINERPATH` with the specified `OPTIONS`.
    * The `ro` option will make the volume mount inside the container read-only.
    * If no options are defined, the container by default will have read and write access to the volume.
    * Ready made containers usually have instructions on where to mount what on their dockerhub page. See https://hub.docker.com/_/nginx for example.
* Navigate to `http://localhost/8080` on your browser and ensure you are greeted with the `Hello, Aslan!` message.
* Run `docker stop nginx` to stop the nginx container.

## Gotchas

* On Windows using Git Bash, you must replace `$(PWD)` with `${PWD:0:2}:${PWD:2}` due to the ever so nice drive letter system Windows has.
* Full command on Windows using Git Bash then becomes `docker run --rm --name nginx -v ${PWD:0:2}:${PWD:2}/html:/usr/share/nginx/html:ro -d -p 8080:80 nginx`

## Expected output

```
$ docker run --rm --name nginx -v $(PWD)/html:/usr/share/nginx/html:ro -d -p 8080:80 nginx
c3d71abbf7fb1dbbce23533c80ab21f6d2fe48b71dbddfb79b5601cf32a20932
```

```
$ curl localhost:8080
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   129  100   129    0     0   8600      0 --:--:-- --:--:-- --:--:--  8600<html>
    <head>
        <title>Hello, Aslan!</title>
    </head>
    <body>
        <h1>Hello, Aslan!</h1>
    </body>
</html>
```

## Up next

[04 - Mounting files to Nginx](../04-MountingFilesNginx/04-MountingFilesNginx.md)
