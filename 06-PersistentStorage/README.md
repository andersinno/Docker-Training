# Persistent Storage

## Objective

* Run a container that retains files it creates after a reboot.

## To-do

* Run `docker run -it ubuntu bash`, and inside the container:
   * Run `touch /root/hello.txt`.
   * Run `ls /root/`, and observe the file we just created exists.
   * Run `exit` to exit the container.
* Run `docker run -it ubuntu bash`, and inside the container:
   * Run `ls /root/`, and observe our file no longer exists.
   * This is because containers are read only, and will clear all files that have been written to will be lost once the container stops running.
   * Run `exit`.
* Next we will allocate a named volume to the container, so we can have persistent storage across containers.
* Run `docker run -it -v testvolume:/root/ ubuntu bash`, and inside the container:
   * Run `touch /root/hello.txt`.
   * Run `ls /root/`.
   * Run `exit`.
* Run `docker run -it -v testvolume:/root/ ubuntu bash`, and inside the container:
   * Run `ls /root/`, and observe this time our file still remains there. This is because we mount a named volume on top of the `/root/` folder while booting the container, so anything written to that directory will be actually written on the named volume.
   * Run `exit`.

## Gotchas

* On windows, the container target path when mounting might need prefixing with another `/` like so: `-v testvolume://root/`.

## Extra

* Mounting a volume to a container overrides the contents of the target path inside the container.
* Multiple containers can use the same volume at the same time. This can be useful for example if one container builds static files and another serves the compiled files.

## Expected output

```
root@346745de2804:/# touch /root/hello.txt
root@346745de2804:/# ls /root
hello.txt
root@346745de2804:/# exit
exit
```

```
$ docker run -it ubuntu bash
root@65708aab62eb:/# ls /root/
root@65708aab62eb:/# exit
exit
```

```
$ docker run -it -v testvolume:/root/ ubuntu bash
root@f4358417b75b:/# touch /root/hello.txt
root@f4358417b75b:/# ls /root/
hello.txt
root@f4358417b75b:/# exit
exit
```

```
$ docker run -it -v testvolume:/root/ ubuntu bash
root@1d22d6ba4c97:/# ls /root/
hello.txt
root@1d22d6ba4c97:/# exit
exit
```

## Up next

[07 - Cleanup](../07-Cleanup/README.md)
