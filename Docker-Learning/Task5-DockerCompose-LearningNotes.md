
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



































### Reference: ###
1. [使用Docker Compose部署应用详解](https://blog.csdn.net/u013071319/article/details/107123677/)
