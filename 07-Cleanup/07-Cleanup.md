# Hello World

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
   * NOTE: It's rare to need to do this, as it can also clear your persistent storages such as databases etc.

## Extra

* If you singular resources need to be removed instead of everything, generally the commad `docker RESOURCETYPE remove NAME` works. The name can also be replaced with the hash of the resource.

## Expected output

```
$ docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
1d75b2b4245431d012118ad197819e086c99c6654d68fc3bb9aec666315d826e
c21f94b812204ca7090cefd8a109dcd6885edcd50aa0119a385cb00017d92e26
940c96c298bc3b0e24fabfa24b473c5d36587f8ea073e43b7666184de033514b
07c874c87024142dcc42be5d3e8918683fa4f663319e2ee8770466b56e9ce960
188da38ede5ec950afe4cc8ddc6f448e9074087db2906e8dac303884e6f15f25
39f78c69e9803c3976e0ce6b3ab235d804f9766b47fd2469b148d16d11ea93ad
aaf0fd34563d5f9482045407177c3b2f3c395efcf15b00b29d2e04d6664a2a57
cd6465f3ba05d5f77fa5270bfc1665a54363da50152a21d9a0b994211c885c45
a76ea90972aae0188ad9638248dc163413d32437f9b4901639d88e004bcd544d
00acacec0c63700a18f6c4b234e8a138233c979dfadc87c806c613de4846ee9c
1913f03c5bad02d7935f68c67f65d657cccbf5942068da7cf0c75cb1abbcd63a
698b83c18abb5963b4d338e04ebdea9682ba5c6978c792122d5855e7eeeb0f14
9b2de95bb248c7804982d5104536b8c419bf8681ecf144e4d59760eb757eccc4
2cb4e2c8143cc8e50f841061f4e9a76b2604234ce584cb8a3c679d64c418eff9
cd07d18ae67d09b41f3e93b81cefa9ad04f2c838a8302d610d02ef5f67c7f868
19429e41735554bf9de985d94400bfd9335fcba2adc5079ce4ebc3ff22683bc5
af6f5a43fc08db5647490fb5c22fbf01df98acbe8d6b1b8c21b400f10c9d09d4
d14dc2d80b04d3e8a7db207bbefe61d22414c0d3b8df1f7e2c66c69c85d879f4

Total reclaimed space: 32.01MB
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
Total reclaimed space: 0B
```
