
### 1. Docker Compose ###

Docker Compose 的前身是 Fig。Fig 是一个由 Orchard 公司开发的强有力的工具，在当时是进行多容器管理的最佳方案。Fig 是一个基于 Docker 的 Python 工具，允许用户基于一个 YAML 文件定义多容器应用，从而可以使用 fig 命令行工具进行应用的部署。Fig 还可以对应用的全生命周期进行管理。内部实现上，Fig 会解析 YAML 文件，并通过 Docker API 进行应用的部署和管理。

在 2014 年，Docker 公司收购了 Orchard 公司，并将 Fig 更名为 Docker Compose。命令行工具也从 fig 更名为 docker-compose，并自此成为绑定在 Docker 引擎之上的外部工具。虽然它从未完全集成到 Docker 引擎中，但是仍然受到广泛关注并得到普遍使用。直至今日，Docker Compose 仍然是一个需要在 Docker 主机上进行安装的外部 Python 工具。使用它时，首先编写定义多容器（多服务）应用的 YAML 文件，然后将其交由 docker-compose 命令处理，Docker Compose 就会基于 Docker 引擎 API 完成应用的部署。


### 2. Example ###

#### 2.1 web 应用 ####
新建文件夹，在该目录中编写 app.py 文件

```python
from flask import Flask
from redis import Redis
import os
import socket

app = Flask(__name__)
redis = Redis(host=os.environ.get('REDIS_HOST', '127.0.0.1'), port=6379)


@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello Container World! I have been seen %s times and my hostname is %s.\n' % (redis.get('hits'),socket.gethostname())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
```

#### 2.2 Dockerfile ###

```
FROM python:2.7
COPY . /app
WORKDIR /app
RUN pip install flask redis
EXPOSE 5000
CMD [ "python", "app.py" ]
```

#### 2.3 docker-compose.yml ####

```
version: "3"

services:

  redis:
    image: redis

  web:
    build:
      context: .
      dockerfile: Dockerfile
    environment:
      REDIS_HOST: redis
```

* `$ docker-compose up -d`

```
Building web
failed to get console mode for stdout: The handle is invalid.
[+] Building 93.2s (10/10) FINISHED
....
Creating webapp_redis_1 ... done

```

* `docker-compose ps -a`

```
     Name                   Command               State    Ports
------------------------------------------------------------------
webapp_redis_1   docker-entrypoint.sh redis ...   Up      6379/tcp
webapp_web_1     python app.py                    Up      5000/tcp
```

* `docker container ls`  

2 services in yaml files docker compose will create 2 containers

```
ONTAINER ID   IMAGE        COMMAND                  CREATED        STATUS       PORTS      NAMES
3b70af619c9f   redis        "docker-entrypoint.s…"   14 hours ago   Up 5 hours   6379/tcp   webapp_redis_1
2f4e6c677752   webapp_web   "python app.py"          14 hours ago   Up 5 hours   5000/tcp   webapp_web_1
```

* `docker-compose stop`

```
Stopping webapp_redis_1 ... done
Stopping webapp_web_1   ... done
```

* `docker-compose start`

```
Starting redis ... done
Starting web   ... done
```

* `docker-compose down`

down则会停止并删除创建的service，volume和network。

* `docker-compose logs`

```
Attaching to webapp_redis_1, webapp_web_1
redis_1  | 1:C 20 Apr 2021 16:26:49.387 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
redis_1  | 1:C 20 Apr 2021 16:26:49.387 # Redis version=6.2.2, bits=64, commit=00000000, modified=0, pid=1, just started
redis_1  | 1:C 20 Apr 2021 16:26:49.387 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
redis_1  | 1:M 20 Apr 2021 16:26:49.387 * monotonic clock: POSIX clock_gettime
redis_1  | 1:M 20 Apr 2021 16:26:49.389 * Running mode=standalone, port=6379.
redis_1  | 1:M 20 Apr 2021 16:26:49.390 # Server initialized
redis_1  | 1:M 20 Apr 2021 16:26:49.390 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or 
run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
redis_1  | 1:M 20 Apr 2021 16:26:49.390 * Ready to accept connections
redis_1  | 1:signal-handler (1618956211) Received SIGTERM scheduling shutdown...
redis_1  | 1:M 20 Apr 2021 22:03:31.068 # User requested shutdown...
redis_1  | 1:M 20 Apr 2021 22:03:31.069 * Saving the final RDB snapshot before exiting.
redis_1  | 1:M 20 Apr 2021 22:03:31.081 * DB saved on disk
redis_1  | 1:M 20 Apr 2021 22:03:31.083 # Redis is now ready to exit, bye bye...
redis_1  | 1:C 20 Apr 2021 22:07:36.844 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
redis_1  | 1:C 20 Apr 2021 22:07:36.845 # Redis version=6.2.2, bits=64, commit=00000000, modified=0, pid=1, just started
redis_1  | 1:C 20 Apr 2021 22:07:36.845 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
redis_1  | 1:M 20 Apr 2021 22:07:36.845 * monotonic clock: POSIX clock_gettime
redis_1  | 1:M 20 Apr 2021 22:07:36.848 * Running mode=standalone, port=6379.
redis_1  | 1:M 20 Apr 2021 22:07:36.848 # Server initialized
redis_1  | 1:M 20 Apr 2021 22:07:36.848 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or 
run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
redis_1  | 1:M 20 Apr 2021 22:07:36.849 * Loading RDB produced by version 6.2.2
redis_1  | 1:M 20 Apr 2021 22:07:36.849 * RDB age 245 seconds
redis_1  | 1:M 20 Apr 2021 22:07:36.849 * RDB memory usage when created 0.77 Mb
redis_1  | 1:M 20 Apr 2021 22:07:36.849 * DB loaded from disk: 0.000 seconds
redis_1  | 1:M 20 Apr 2021 22:07:36.849 * Ready to accept connections
web_1    |  * Serving Flask app "app" (lazy loading)
web_1    |  * Environment: production
web_1    |    WARNING: This is a development server. Do not use it in a production deployment.
web_1    |    Use a production WSGI server instead.
web_1    |  * Debug mode: on
web_1    |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
web_1    |  * Restarting with stat
web_1    |  * Debugger is active!
web_1    |  * Serving Flask app "app" (lazy loading)
web_1    |  * Environment: production
web_1    |    WARNING: This is a development server. Do not use it in a production deployment.
web_1    |    Use a production WSGI server instead.
web_1    |  * Debug mode: on
web_1    |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
web_1    |  * Restarting with stat
web_1    |  * Debugger is active!
```

* yaml file 

```
  version: "3.5"
  services:
    web-fe:
      build: .
      command: python app.py
      ports:
        - target: 5000
          published: 5000
      networks:
        - counter-net
      volumes:
        - type: volume
          source: counter-vol
          target: /code
    redis:
      image: "redis:alpine"
      networks:
        counter-net:
  
  networks:
    counter-net:
  
  volumes:
    counter-vol:

```

* Version 是必须指定的，而且总是位于文件的第一行。它定义了 Compose 文件格式（主要是 API）的版本。建议使用最新版，示例中 Compose 文件将使用版本 3 及以上的版本。注意，version 并非定义 Docker Compose 或 Docker 引擎的版本号。

* Services 用于定义不同的应用服务。上边的例子定义了两个服务：一个名为 web-fe 的 Web 前端服务以及一个名为 redis 的内存数据库服务。Docker Compose 会将每个服务部署在各自的容器中。

* Networks 用于指引 Docker 创建新的网络。默认情况下，Docker Compose 会创建 bridge 网络。这是一种单主机网络，只能够实现同一主机上容器的连接。当然，也可以使用 driver 属性来指定不同的网络类型。下面的代码可以用来创建一个名为 over-net 的 Overlay 网络，允许独立的容器（standalone container）连接（attachable）到该网络上。

* volumes 用于指引 Docker 来创建新的卷。上面例子中的 Compose 文件使用的是 v3.5 版本的格式，定义了两个服务，一个名为 counter-net 的网络和一个名为 counter-vol 的卷。

web-fe 的服务定义中，包含如下指令。

*build*
  指定 Docker 基于当前目录（.）下 Dockerfile 中定义的指令来构建一个新镜像。该镜像会被用于启动该服务的容器。

*command*
  python app.py 指定 Docker 在容器中执行名为 app.py 的 Python 脚本作为主程序。因此镜像中必须包含 app.py 文件以及 Python，这一点在 Dockerfile 中可以得到满足。

*ports*
  指定 Docker 将容器内（-target）的 5000 端口映射到主机（published）的 5000 端口。这意味着发送到 Docker 主机 5000 端口的流量会被转发到容器的 5000 端口。容器中的应用监听端口 5000。

*networks*
  使得 Docker 可以将服务连接到指定的网络上。这个网络应该是已经存在的，或者是在 networks 一级 key 中定义的网络。对于 Overlay 网络来说，它还需要定义一个 attachable 标志，这样独立的容器才可以连接上它（这时 Docker Compose 会部署独立的容器而不是 Docker 服务）。

*volumes*
  指定 Docker 将 counter-vol 卷（source:）挂载到容器内的 /code（target:）。counter-vol 卷应该是已存在的，或者是在文件下方的 volumes 一级 key 中定义的。

  综上，Docker Compose 会调用 Docker 来为 web-fe 服务部署一个独立的容器。该容器基于与 Compose 文件位于同一目录下的 Dockerfile 构建的镜像。基于该镜像启动的容器会运行 app.py 作为其主程序，将 5000 端口暴露给宿主机，连接到 counter-net 网络上，并挂载一个卷到/code。

`注： 从技术上讲，本例并不需要配置 command: python app.py。因为镜像的 Dockerfile 已经将 python app.py 定义为了默认的启动程序。但是，本例主要是为了展示其如何执行，因此也可用于覆盖 Dockerfile 中配置的 CMD 指令。`

Redis 服务的定义相对比较简单:

*image*
  redis:alpine 使得 Docker 可以基于 redis:alpine 镜像启动一个独立的名为 redis 的容器。 这个镜像会被从 Docker Hub 上拉取下来。

*networks*
  配置 redis 容器连接到 counter-net 网络。

 由于两个服务都连接到 counter-net 网络，因此它们可以通过名称解析到对方的地址。了解这一点很重要，本例中上层应用被配置为通过名称与 Redis 服务通信。
 
 

* Creating a Spark Standalone Cluster with Docker and docker-compose

 ![image](https://user-images.githubusercontent.com/39177230/115524841-1f277700-a2c1-11eb-97f4-9f10889a6935.png)

 运行结果:
 
 `docker container ls`
 
 ![image](https://user-images.githubusercontent.com/39177230/115530040-ff468200-a2c5-11eb-8697-63e5c9dd2ebf.png)
 
 ![image](https://user-images.githubusercontent.com/39177230/115530569-7a0f9d00-a2c6-11eb-8d07-868fa4f0829e.png)

 
 [source](https://github.com/mvillarrealb/docker-spark-cluster)
































### Reference: ###
1. [使用Docker Compose部署应用详解](https://blog.csdn.net/u013071319/article/details/107123677/)
2. [Creating a Spark Standalone Cluster with Docker and docker-compose](https://medium.com/@marcovillarreal_40011/creating-a-spark-standalone-cluster-with-docker-and-docker-compose-ba9d743a157f)
3. 
