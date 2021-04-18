* `docker container ls`

```
CONTAINER ID   IMAGE          COMMAND                  CREATED        STATUS        PORTS                   NAMES
8578669c0c8a   nginx:alpine   "/docker-entrypoint.…"   19 hours ago   Up 19 hours   0.0.0.0:49157->80/tcp   reverent_noether
```

* `docker container stop 8578669c0c8a`

```
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

* `docker run -d -P nginx:alpine` 
* `docker container ls`

```
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                   NAMES
2ec886612108   nginx:alpine   "/docker-entrypoint.…"   25 seconds ago   Up 22 seconds   0.0.0.0:49158->80/tcp   silly_rhodes
```

* `docker logs 2ec886612108`

```
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
172.17.0.1 - - [18/Apr/2021:09:08:05 +0000] "GET / HTTP/1.1" 200 612 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77" "-"
172.17.0.1 - - [18/Apr/2021:09:08:05 +0000] "GET /favicon.ico HTTP/1.1" 404 556 "http://localhost:49158/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77" "-"
2021/04/18 09:08:05 [error] 33#33: *1 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost:49158", referrer: "http://localhost:49158/"
```

* `docker run -d -p 127.0.0.1:80:80 nginx:alpine`

```
docker: Error response from daemon: Ports are not available: listen tcp 127.0.0.1:80: bind: An attempt was made to access a socket in a way forbidden by its access permissions
```

* `docker port 2ec886612108 80`
```
0.0.0.0:49158
```
### 新建网络 ###
* `docker network create -d bridge my-net`

### 连接容器 ###
* `docker run -it --rm --name busybox2 --network my-net busybox sh`
* `docker run -it --rm --name busybox2 --network my-net busybox sh`

```
/ # ping busybox1
PING busybox1 (172.19.0.2): 56 data bytes
64 bytes from 172.19.0.2: seq=0 ttl=64 time=0.202 ms
64 bytes from 172.19.0.2: seq=1 ttl=64 time=0.132 ms
64 bytes from 172.19.0.2: seq=2 ttl=64 time=0.125 ms
64 bytes from 172.19.0.2: seq=3 ttl=64 time=0.126 ms
64 bytes from 172.19.0.2: seq=4 ttl=64 time=0.143 ms
64 bytes from 172.19.0.2: seq=5 ttl=64 time=0.072 ms
^C
--- busybox1 ping statistics ---
6 packets transmitted, 6 packets received, 0% packet loss
round-trip min/avg/max = 0.072/0.133/0.202 ms
```

```
 # ping busybox2
PING busybox2 (172.19.0.3): 56 data bytes
64 bytes from 172.19.0.3: seq=0 ttl=64 time=0.038 ms
64 bytes from 172.19.0.3: seq=1 ttl=64 time=0.124 ms
64 bytes from 172.19.0.3: seq=2 ttl=64 time=0.094 ms
^C
--- busybox2 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 0.038/0.085/0.124 ms
```


* `docker container ls`

```
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                   NAMES       
f6729bf55103   busybox        "sh"                     21 seconds ago   Up 19 seconds                           busybox2    
dd74ca72d851   busybox        "sh"                     7 minutes ago    Up 7 minutes                            busybox1    
2ec886612108   nginx:alpine   "/docker-entrypoint.…"   28 minutes ago   Up 28 minutes   0.0.0.0:49158->80/tcp   silly_rhodes
```

busybox1 容器和 busybox2 容器建立了互联关系

### 配置DNS ###

* `docker run -it --rm ubuntu:18.04  cat etc/resolv.conf`
```
Unable to find image 'ubuntu:18.04' locally
18.04: Pulling from library/ubuntu
6e0aa5e7af40: Pull complete
d47239a868b3: Pull complete
49cbb10cca85: Pull complete
Digest: sha256:122f506735a26c0a1aff2363335412cfc4f84de38326356d31ee00c2cbe52171
Status: Downloaded newer image for ubuntu:18.04
# This file is managed by man:systemd-resolved(8). Do not edit.
#
# This is a dynamic resolv.conf file for connecting local clients directly to
# all known uplink DNS servers. This file lists all configured search domains.
#
# Third party programs must not access this file directly, but only through the
# symlink at /etc/resolv.conf. To manage man:resolv.conf(5) in a different way,
# replace this symlink by a static file or a different symlink.
#
# See man:systemd-resolved.service(8) for details about the supported modes of
# operation for /etc/resolv.conf.

nameserver 168.63.129.16
search eyupuaqrvjuexhukix0kqta5md.bx.internal.cloudapp.net
```

### Docker的网络模式 ###

* `docker network ls`

```
NETWORK ID          NAME                DRIVER              SCOPE
14262a84333c        bridge              bridge              local
cd16cefef635        host                host                local
c077cc00f730        my-net              bridge              local
7cfaa96d8335        none                null                local
```

![image](https://user-images.githubusercontent.com/39177230/115141561-a9789c80-a06f-11eb-978e-02e2eb5752c7.png)




