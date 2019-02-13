# Hello World

## Objective

* Run a docker container based on the `ubuntu` container image
* Open an interactive bash session on the container

## To-do

* Run `docker run -it ubuntu bash` on your terminal.
   * The `-i` flag stands for `--interactive`, and makes the container keep the
   STDIN open for input
   * The `-t` (or `--tty`) flag will allocate a pseudo-TTY to the container
   * This should result in an interactive bash session inside the container
* Try running commands inside the container
   * Running destructive commands (such as `rm -rf /`) is fine and will not affect the host OS
   * If you run destructive commands, make sure you are
   _actually_ inside the container first

## Gotchas

* On windows, you will need to use [winpty](https://github.com/rprichard/winpty) to
handle the pseudo-TTY provided by Docker. You can do this by prefixing the command
with `winpty`, so for example `winpty docker run -it ubuntu bash`
   * It is recommended to use an alias for the `docker` command with `winpty`
   already prefixed. This can be done by adding `alias docker="winpty docker"` to
   `~/.profile`, if using Git Bash.
   * Windows cmd and powershell also supports aliases, but it's up to the user to
   figure out how those are configured.

## Expected output
```
$ docker run -it ubuntu bash
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
6cf436f81810: Pull complete
987088a85b96: Pull complete
b4624b3efe06: Pull complete
d42beb8ded59: Pull complete
Digest: sha256:7a47ccc3bbe8a451b500d2b53104868b46d60ee8f5b35a24b41a86077c650210
Status: Downloaded newer image for ubuntu:latest
root@c21f94b81220:/# ls
bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@c21f94b81220:/# exit
```
