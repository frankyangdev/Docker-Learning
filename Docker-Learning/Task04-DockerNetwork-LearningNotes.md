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

* `docker network create -d bridge my-net`

```
PING busybox1 (172.19.0.2): 56 data bytes
64 bytes from 172.19.0.2: seq=0 ttl=64 time=0.183 ms
64 bytes from 172.19.0.2: seq=1 ttl=64 time=0.094 ms
64 bytes from 172.19.0.2: seq=2 ttl=64 time=0.085 ms
64 bytes from 172.19.0.2: seq=3 ttl=64 time=0.108 ms
^C
--- busybox1 ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 0.085/0.117/0.183 ms
```



