# Cleanup

## Objective

* Clean up unused containers and images to reclaim space

## To-do

* Run `docker container prune`
   * This will remove all currently stopped containers from the docker engine
* Run `docker image prune`
   * This will remove all unused docker images from the disk. In-use (even on stopped containers) images will not be removed.
* Run `docker network prune`
   * This will remove all networks not in use by at least a single container.
* Run `docker volume prune`
   * This will remove all volumes not in use by containers.
   * **NOTE**: It's rare to need to do this, as it can also clear your persistent storages such as databases etc.

## Extra

* If you singular resources need to be removed instead of everything, generally the commad `docker RESOURCETYPE remove NAME` works. The name can also be replaced with the hash of the resource.

## Expected output

```
$ docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
1d22d6ba4c97919010beefd54c6641452efb797e4d98f8de89943dc2945de2e3
f4358417b75b9bf2d9a66241ae8379df6926c3573f593f617bdfb1e91478eb39
65708aab62eb3cbf79cae744bb037a3d617f1d7ca32ce35b42b7fd759d2d7153
346745de2804a26deca57e168743539ef818aa5038c28eb1e8104370c2b9bf6d
40c5f6008a1434064241a8b577a03b1809d911f3359d0a1979abddd73ded01ce
61208e8b3bff34f255e8969531ab60366cec0099b7987986b72c140bfbd76e35
71a8842baf9936dffda32b61ebfa7f7217c66fafefc5de18d96453d63c520737
d66e21e269a1ce5e800fa0ca995219b06ad34cc55e8701f2054a912ae25dd8d5

Total reclaimed space: 104.5kB
```

```
$ docker image prune
WARNING! This will remove all dangling images.
Are you sure you want to continue? [y/N] y
Deleted Images:
deleted: sha256:fdf31ecbbee7183a6d948c610b6f8038265e1cd0d0f3b3ed0ba4030f59340dfd
deleted: sha256:88db1669a1e6b117ec668efaf70b056f9865c5409f40196501854b4f4e9acb0b
deleted: sha256:9a7c6e9c605e4f6db03255aafa81ae72e45b620f5b7b97279674ea633f469346
deleted: sha256:1184743ff6301927671e3f1056b79493775d0c5423d89fe7dbf64c8ecf80d611
deleted: sha256:74b0b5dec25cc85d4c7b215408158dd6237009300dbb6923abb1df8921b32d32
deleted: sha256:87844e1cf01b79764b58f7dec2533c8e05d8faf24aea2497dbbc64c9f77f5701
deleted: sha256:8e648ad9d9fae705caf2d8ddca0dc322b811179b13876e89beb066b0bb750c5f
deleted: sha256:ca76711d9c53763dd239cc89ef683f17b1ce26fe928484257d4f614246151ece
deleted: sha256:9356f526e2b2c1587c320d187bbded1ba4ef4dc081a980c741980bd5787bcce7
deleted: sha256:26040dee684c3f64a95373388d6a4592ac2ef4724dec26f5e66cc452d88bd79e
deleted: sha256:7332b49c23b08e1b53afe0100598f98f7b905badf0fe955b479685e612bb9b96
deleted: sha256:af110379dfaecbaf643f56199435ca1062685c63e58c98f510353ecf28d4436e
deleted: sha256:f68d2185e9cdba1e695203a4556f402b094e62c6a1ae8d05b44c96db90e92cd0
deleted: sha256:8f45142483f3330c3b884ca42d929d68e099d47baa221994f2ecc0401117542c
deleted: sha256:e61d0b9aa0f45fd1a4f73fc8404a1eb0d53a59863469594d842ace86c5ebd265
deleted: sha256:0b127a2edc00fbbbb8c30dd689a3d554b9b8a638d2ec88b3b745da8fb2f92e81
deleted: sha256:a6e8f228ee3215735e5ef1e8dcfe8a6d318e8a843e027909fd1538421eb474a4
deleted: sha256:5782102ea1d53ae9a0cab80cd568b3aa3a7e20792f2a6a9d07dff38458f1bd12
deleted: sha256:099f82dce11419161a04c2b4d3d91635ca307ebd8d8cb4de047e3ad37781efd8
deleted: sha256:0e3737a098edfbb0cfa9bc18a6dac668779b35bfe6fbe72601213334e57e209e
deleted: sha256:e266178ef7577e62c56e5233baac1239291e7a84185bc8e6e78efd48db683e12
deleted: sha256:d195b8f5a93cc255e13a6a286c0a19c89a400587033ab7fb544e4ee0e94cbd95
deleted: sha256:b4289c93d46da4202a83bb19fb97180ac5b1acb4c7be902d7e1cf451b4b8dd14
deleted: sha256:c70b1ec1749cf97f351a4e248340f8b5a0b7edd61df8bae995c80d86bc1e2660
deleted: sha256:552b8b9e0cb65ce10a0dd51fac087c86b5114471bf2ebed22411a4190dc2c8fa
deleted: sha256:5a174f44e0b5e865426738c56d3eac354bdf779785702698c2cb09aa4b889e25
deleted: sha256:294c7e498e94b776694311b4929be8f0cb00f1c88aaa94d8ae61d7e018cc87a0
deleted: sha256:603f049c403ebf66281ca9d21bf11ea36077de096bd20d0275a71ca260a16d9e
deleted: sha256:29c50e2e2eeb2a4f4c8183474eda7f863e7abd8e3b55c96dc6d94357936be0bf

Total reclaimed space: 1.683GB
```

```
$ docker network prune
WARNING! This will remove all networks not used by at least one container.
Are you sure you want to continue? [y/N] y
Deleted Networks:
reaktor-overmind-challenge-2019_default
contty_default
```

```
$ docker volume prune
WARNING! This will remove all local volumes not used by at least one container.
Are you sure you want to continue? [y/N] y
Deleted Volumes:
testvolume
3a5514a849511ecbb63b1f7ce10f0c58cf5fa34a9a9791b23ac79ab8aefd56ce
7d216abd957e913fdc025d00e990d7e48c0fd31f6b70e34855d7c080376af05d

Total reclaimed space: 379.1MB
```
