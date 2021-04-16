### 命令实践 ###


```
docker volume
```

![image](https://user-images.githubusercontent.com/39177230/115022091-7a3b2180-9eef-11eb-8af3-f61cae327fd2.png)


```
docker volume inspect datawhale
```

![image](https://user-images.githubusercontent.com/39177230/115022237-b1a9ce00-9eef-11eb-8564-7c18c5ef0610.png)


```
docker run -d -P --name web --mount source=datawhale,target=/usr/share/nginx/html nginx:alpine
```

![image](https://user-images.githubusercontent.com/39177230/115022827-84115480-9ef0-11eb-9c5e-a7d0bf37f730.png)



```
docker inspect web
```

![image](https://user-images.githubusercontent.com/39177230/115023079-e0747400-9ef0-11eb-9e3c-5803a4d9dc0d.png)

* **we can see the container web with volume  has mounted to target**

![image](https://user-images.githubusercontent.com/39177230/115023395-511b9080-9ef1-11eb-8be4-945956a476e9.png)

![image](https://user-images.githubusercontent.com/39177230/115024128-3eee2200-9ef2-11eb-84d0-824714cd4faf.png)

* **check web server if it is running**

![image](https://user-images.githubusercontent.com/39177230/115023928-f9c9f000-9ef1-11eb-8d2a-f4228e71eda6.png)


* **when delete volume but failed to delete due to volume is in use, that means the container and web instance are using the volume. Have to stop container and then delete volume**


```
docker volume rm datawhale
Error response from daemon: remove datawhale: volume is in use - [1f2526e9e107a5d326b56898a67b51e9eb21904e704f1ea779441c6f18b7f78f]

docker stop 1f2526e9e107a5d326b56898a67b51e9eb21904e704f1ea779441c6f18b7f78f

docker rm 1f2526e9e107a5d326b56898a67b51e9eb21904e704f1ea779441c6f18b7f78f 

docker volume rm datawhale

docker volume ls
```


* **以下命令加载主机的 /src/webapp 目录到容器的 /usr/share/nginx/html目录。这个功能在进行测试的时候十分方便，比如用户可以放置一些程序到本地目录中，来查看容器是否正常工作。本地目录的路径必须是绝对路径如果挂载的目录不存在，创建容器时，docker 不会自动创建，此时会报错.**

```
$ docker run -d -P \
    --name web \
    --mount type=bind,source=/src/webapp,target=/usr/share/nginx/html,readonly \
    nginx:alpine

```













