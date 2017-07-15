---
date: "2016-12-31T11:03:14+08:00"
title: "Dockerfile 简单使用实例"
menu: "main"
Categories: ["Development","Docker"]
Tags: ["Development","Docker"]
Description: "介绍 Docker Dockerfile 的简单使用方法和示例"
---

## 如何使用

Dockerfile 用来创建一个image,包含了用户安装的软件依赖等。

例: 当前目录下包含Dockerfile,使用命令build来创建新的image,并命名为 explame/explame:v1

    docker built -t explame/explame:v1 .

<!--more-->

## Dockerfile 关键字

### Dockerfilede 的基本格式

    # Comment
    INSTRUCTION agruments

### FROM

基于某个镜像，例:

    FROM ubuntu:14.04

### RUN

执行镜像构建、安装等。

    RUN echo hello

### MAINTAINER

镜像构建者信息等。

    MAINTAINER XXX < XX@XX.com >

### CMD

容器启动时执行的命令，Dockerfile 只能包含一个 CMD ，多个只执行最后一个。
CMD 主要用于容器启动时默认执行的命令，当Docker run command的命令匹配到CMD command时，会替换CMD执行的命令。格式如:

    CMD echo hello world
    CMD ["echo", "hello world"]

### ENTRYPOINT

类似于CMD，区别在于命令不可替换，和 CMD 可组合使用。例:

   ENTRYPOINT ["/bin/echo"]
   CMD ["hello word"]

### USER

指定容器运行时的用户。

### EXPOSE

暴露容器的端口，使宿主机能够通过 `docker run -p` 使用。例:

    EXPOSE port
    EXPOSE port1 port2 port3

    docker run -p port
    docker run -p host_port1:port1 -p host_port2:port2 host_port3:port3 ...

### ENV

设置变量，在 `RUN` 构建镜像以及容器启动后均可使用的变量。例:

    ENV HOME /root

### ADD 与 COPY

容器构建时的命令，构建时命令将文件从容器外复制到容器内，两者区别在于ADD能从网络中下载。所有复制到容器内的文件及文件夹权限为 755 ，uid 、 gid 为 0 。如果复制的源为目录，则将目录下的文件全部复制到指定地,不包括目录;复制源为可识别的压缩文件，docker自动解压到到容器内指定位置;如何复制源为文件且复制目标不以 `/` 结束时，docker将文件复制到容器内并改名为指定名字。

### VOLUME

构建时命令。允许本地文件挂在到容器中。

### WORKDIR

构建时命令。重置容器的当前工作路径。

### ONBUILD

构建不运行，容器使用时运行的命令。
