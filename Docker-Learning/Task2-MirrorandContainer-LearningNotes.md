
### 1. 镜像常用命令 ###

![image](https://user-images.githubusercontent.com/39177230/114905338-6d64f200-9e4b-11eb-846c-c1b59f249dc0.png)

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

5. 镜像下载加速1、使用 Maven 时会从 Maven 中央仓库下载依赖，默认从官方中央仓库下载时会很慢，于是大家就会修改配置文件，设置为国内的中央仓库下载地址，此时速度就没问题了。

2、同理 Docker 也是一样，默认从 docker 官网仓库下载镜像时会很慢，也需要修改为国内仓库地址。

```
网易：http://hub-mirror.c.163.com

ustc：https://docker.mirrors.ustc.edu.cn

中国科技大学：https://docker.mirrors.ustc.edu.cn
```



[Docker 镜像、容器 常用命令 与 操作](https://blog.csdn.net/wangmx1993328/article/details/81735070)




