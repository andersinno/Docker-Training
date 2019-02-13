# Exposing Nginx

## Objective

* Run a docker container based on the `nginx` container image.
* Expose the Nginx port from the container to the host.
* Use the `docker ps` command to view the status of running containers.
* Use the `docker stop` command to stop the nginx container.

## To-do

* Run `docker run --rm --name nginx -d -p 8080:80 nginx` on your terminal.
    * The `--rm` flag will make docker remove the container automatically once it exits. If this is not used, it can also be manually removed with `docker container rm NAME`.
    * The `--name NAME` option will set the container's name to the provided value. This can later on be used to refer to the container when running commands against it.
    * The `-d` flag will make the container run in the background.
    * The `-p HOSTPORT:CONTAINERPORT` will publish the `CONTAINERPORT` port from within the containere and make it available at `HOSTPORT` on the host.
        * You can (and should) also define the host address, unless intending to expose the service publicly. This can be done with `-p LISTENADDRESS:HOSTPORT:CONTAINERPORT`.
        * For example: `-p 127.0.0.1:8080:80`.
* Run `docker ps` and make sure the nginx container is running.
* Navigate to `http://localhost/8080` on your browser and ensure you are greeted with the `Welcome to nginx!` message.
* Run `docker stop nginx` to stop the nginx container.
    * Here we can refer to the container as `nginx`, as we earlier defined that to be the container's name with the `--name nginx` option.
* Run `docker ps` and make sure the nginx container has stopped.


## Expected output
```
$ docker run -p 8080:80 nginx
Unable to find image 'nginx:latest' locally
latest: Pulling from library/nginx
6ae821421a7d: Pull complete
da4474e5966c: Pull complete
eb2aec2b9c9f: Pull complete
Digest: sha256:dd2d0ac3fff2f007d99e033b64854be0941e19a2ad51f174d9240dda20d9f534
Status: Downloaded newer image for nginx:latest
d7509515dc2da1a04875fdda6f5036c1b7fe3a3701a4bfaf4f04ae233de09967
```

```
$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS                    NAMES
d7509515dc2d        nginx               "nginx -g 'daemon of…"   About a minute ago   Up About a minute   127.0.0.1:8080->80/tcp   nginx
```

```
$ curl localhost:8080
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   612  100   612    0     0  40800      0 --:--:-- --:--:-- --:--:-- 40800<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

```
$ docker stop nginx
nginx
```

```
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```

```
$ curl localhost:8080
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0curl: (7) Failed to connect to localhost port 8080: Connection refused
```

## Up next

[04 - Mounting files to Nginx](../04-MountingFilesNginx/README.md)
