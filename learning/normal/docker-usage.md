# Docker的基本使用

## Docker基本命令
* docker exec -it 'id' --进入docker容器
* docker run -t -i -p 80:80 镜像 /bin/bash --使用bash打开一个伪终端
* docker serach '镜像' --docker hub 查找镜像
* docker pull '镜像' --docker hub 下载镜像

## DVWA
* docker run --rm -it -p 80:80 vulnerables/web-dvwa
