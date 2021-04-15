
### 1. 镜像和容器 ###

镜像（Image）就是一堆只读层（read-only layer）的统一视角

![image](https://user-images.githubusercontent.com/39177230/114907858-17de1480-9e4e-11eb-8748-89bafc6365ea.png)



容器（container）的定义和镜像（image）几乎一模一样，也是一堆层的统一视角，唯一区别在于容器的最上面那一层是可读可写的。

![image](https://user-images.githubusercontent.com/39177230/114907895-22001300-9e4e-11eb-91b2-a98cef8ab3a6.png)



### 2. 镜像常用命令 ###

![image](https://user-images.githubusercontent.com/39177230/114906261-71454400-9e4c-11eb-8177-6768ab7e7735.png)



1. 检索云端镜像 (i.e mysql)
 
```
docker search mysql
```

2. 下载镜像

```
docker pull docker.io/mysql
or 
docker pull docker.io/mysql:5.7.31
```

3. 查看本地镜像
```
docker images
```

REPOSITORY ：仓库，即下载的镜像名称

TAG：标识，通常为版本号

IMAGE ID：镜像id，删除时可以根据镜像 id 进行删除

CRREATED：镜像创建时间

SIZE：镜像大小

4. 删除镜像

```
docker rmi image-id 

```

5. 镜像下载加速

* 使用 Maven 时会从 Maven 中央仓库下载依赖，默认从官方中央仓库下载时会很慢，于是大家就会修改配置文件，设置为国内的中央仓库下载地址，此时速度就没问题了。

* 同理 Docker 也是一样，默认从 docker 官网仓库下载镜像时会很慢，也需要修改为国内仓库地址。

```
网易：http://hub-mirror.c.163.com

ustc：https://docker.mirrors.ustc.edu.cn

中国科技大学：https://docker.mirrors.ustc.edu.cn
```

6.
```
systemctl daemon-reload

service docker restart
```

### 3. 容器常用操作 ###


1. 查看容器

```
docker ps
```
CONTAINER ID：容器 di
IMAGE：镜像名称:Tag
COMMAND：命令
CREATES：容器创建的时刻
STATUS：容器当前的状态 (up 表示运行、Exited 表示停止运行)
PORTS：镜像程序使用的端口号
NAMES：容器自定义名称

2. 运行容器

```
docker run --name container-name:tag -d image-name
```
--name：自定义容器名，不指定时，docker 会自动生成一个名称

-d：表示后台运行容器

image-name：指定运行的镜像名称以及 Tag

3. 停止容器

```
docker stop container-name|container-id
```

4. 启动容器

```
docker start container-name|container-id
```

5. 删除容器

```
docker rm container-id 
```

6. 查看容器日志

```
docker logs container-name|container-id ：根据容器名或者容器 id 查看容器日志信息。
```

7. 容器端口映射

```docker run --name container-name -d image-name:tag：单纯的如此运行容器，程序占用的是 Docker 容器内部的端口，并不是服务器对外的访问端口，所以必须做 端口映射 将服务器的实际端口映射到 Docker 容器中的端口才能访问

docker run --name container-name:tag -d -p 服务器端口:Docker端口 image-name：端口映射

--name：自定义容器名，不指定时，docker 会自动生成一个名称

-d：表示后台运行容器

-p：表示 Linux 服务器与 Docker 容器的端口映射，默认情况下容器中镜像占用的端口是 Docker 容器中的端口，与外界是隔绝的，必须进行端口映射才能访问。

image-name：指定运行的镜像名称以及 Tag

docker run --name tomcat1 -d -p 8080:8080 tomcat:8.5.32       #运行容器
docker run --name tomcat2 -d -p 8090:8080 tomcat:8.5.32       #运行容器

docker ps -a                                                                                #查看容器
docker logs tomcat1                                                                   #查看容器运行日志
docker logs tomcat2                                                                   #查看容器运行日志

firewall-cmd --zone=public --list-port                                          #查看防火墙开放的端口
firewall-cmd --zone=public --add-port=8080/tcp --permanent    #防火墙开放 8080 端口
firewall-cmd --zone=public --add-port=8090/tcp --permanent    #防火墙开放 8090 端口
firewall-cmd --reload                                                                   #重启防火墙，端口配置才能生效

ip addr show                                                                               #查看 linux 服务器 ip 地址


```









**Reference：**

[Docker 镜像、容器 常用命令 与 操作](https://blog.csdn.net/wangmx1993328/article/details/81735070)

[Docker容器 常用命令 与 操作](https://blog.csdn.net/wangmx1993328/article/details/81735070)

[深入理解Docker容器和镜像](https://blog.csdn.net/u012811805/article/details/106547497)




