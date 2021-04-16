### 1. 命令实践 ###


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

* **we can see the container web with volume info**

![image](https://user-images.githubusercontent.com/39177230/115023395-511b9080-9ef1-11eb-8be4-945956a476e9.png)

![image](https://user-images.githubusercontent.com/39177230/115024128-3eee2200-9ef2-11eb-84d0-824714cd4faf.png)

* **check web server if it is running**

![image](https://user-images.githubusercontent.com/39177230/115023928-f9c9f000-9ef1-11eb-8d2a-f4228e71eda6.png)







