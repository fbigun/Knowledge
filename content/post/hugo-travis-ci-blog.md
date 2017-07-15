---
date: "2017-01-16T23:18:41+08:00"
title: "hugo 利用 travis-ci 持续集成生成静态博客部署在github"
menu: "main"
Categories: ["Development","GoLang"]
Tags: ["Development","golang"]
Description: ""
---

## 描述

> * `Hugo`是由`Go`语言实现的静态网站生成器。简单、易用、高效、易扩展、快速部署。
> * `Travis CI`是在软件开发领域中的一个在线的，分布式的持续集成服务，用来构建及测试在 `GitHub` 托管的代码。这个软件的代码同时也是开源的，可以在 `GitHub` 上下载到，尽管开发者当前并不推荐在闭源项目中单独使用它。
> * `github.com` `coding.net`两个网站为本次博客示例的两个部署点。

<!--more-->

## hugo 使用方法

使用 hugo 生成博客的生成器，先获取 hugo 二进制文件，在 windows/linux/mac/unix 等系统下均有相关的二进制文件，也可使用源码编译生成二进制文件使用。

### 创建站点

```shell
hugo new site <站点名称/路径>
hugo new site . #在当前目录下创建站点
```

### 获取 hugo 博客系统的主题

在 [hugoThemes](https://github.com/spf13/hugoThemes) 上获取主题文件放在站点源文件 `themes` 文件夹下。或者使用 `git subtree` 管理主题。用法如下：

```shell
git subtree add [--squash] -P <prefix> <commit>
git subtree add [--squash] -P <prefix> <repository> <refspec>
```

### 提交文章

```shell
hugo new welcome.md  #生成文章的 markdown 文档文件
hugo new post/first.md  #生成的文件在 `content/post/` 目录下,成为分类。
```

### 调试部署

```shell
hugo server --bind="0.0.0.0" --appendPort=false -p 80 -b http://XXX.com
```

通过apache2反向代理，需要加上`--appendPort=false`，否则转换后的public下面的url地址都会带上你的hugo端口（1313）。

## Travis CI 使用方法

### 基础构建脚本

Travis CI使用YAML文件作为构建脚本，在项目根目录创建.travis.yml文件。

### demo使用方式

```yml
language: android   # 声明构建语言环境

notifications:      # 每次构建的时候是否通知，如果不想收到通知邮箱（个人感觉邮件贼烦），那就设置false吧
  email: false

sudo: false         # 开启基于容器的Travis CI任务，让编译效率更高。

android:            # 配置信息
  components:
    - tools
    - build-tools-23.0.2              
    - android-23                     
    - extra-android-m2repository     # Android Support Repository
    - extra-android-support          # Support Library

before_install:     
 - chmod +x gradlew  # 改变gradlew的访问权限

script:              # 执行:下面的命令
  - ./gradlew assembleRelease  

before_deploy:       # 部署之前
  # 使用 mv 命令进行修改apk文件的名字
  - mv app/build/outputs/apk/app-release.apk app/build/outputs/apk/buff.apk  

deploy:              # 部署
  provider: releases # 部署到GitHub Release，除此之外，Travis CI还支持发布到fir.im、AWS、Google App Engine等
  api_key:           # 填写GitHub的token （Settings -> Personal access tokens -> Generate new token）
    secure: 7f4dc45a19f742dce39cbe4d1e5852xxxxxxxxx
  file: app/build/outputs/apk/buff.apk   # 部署文件路径
  skip_cleanup: true     # 设置为true以跳过清理,不然apk文件就会被清理
  on:     # 发布时机           
    tags: true       # tags设置为true表示只有在有tag的情况下才部署
```

* 因为Repo是Android项目，所以构建语言language选择android。
* 选择了Android项目后，就在android中的components的tag中设置Android项目需要的依赖。
* Travis CI编译Android实际上也是调用项目中的构建脚本的。现在大部分Android项目都是用Gradle构建的，如果是要打Release版本的APK包，在script加入./gradlew assembleRelease就行了。
* Travis CI每次任务完成之后，就会把所有生成的文件清掉,skip_cleanup这个Tag要设置为True，不这样做的话，Travis CI在部署之前就会清空生成的APK文件，那样你就什么都得不到了。
* Travis CI默认支持发布到Github Release上，不需要配置别的脚本;如果不想那么麻烦的话，可以使用Travis CI提供的travis命令行工具。

###  travis 使用方法

```shell
gem install travis -v 1.8.0 --no-rdoc --no-ri
travis setup releases   # 安装 github Release
travis encrypt "SOMESTRING=VALUESTRING"    # 加密字符串，以`key-value`形式
travis encrypt-file super_secret.txt --add # 加密文件,并且添加解密命令到 .travis.yml
```

## hugo博客travis.yml文件内容

```yml
language: go
go:
- master

branches:
  only:
  - hugo

before_install:
- openssl aes-256-cbc -K $encrypted_278ded750974_key -iv $encrypted_278ded750974_iv -in travis-CI-key.enc -out ~/.ssh/id_rsa -d
- sudo chmod 600 ~/.ssh/id_rsa

install:
- curl -LO https://github.com/spf13/hugo/releases/download/v0.18.1/hugo_0.18.1_Linux-64bit.tar.gz
- tar zxf hugo_0.18.1_Linux-64bit.tar.gz
- sudo mv hugo_0.18.1_linux_amd64/hugo_0.18.1_linux_amd64 /bin/hugo

addons:
  ssh_known_hosts: git.coding.net

script:
- hugo --baseURL //fbigun.github.io/
- cd ./public
- git init
- git config user.name "fbigun"
- git config user.email "rsdhlz@qq.com"
- git add -A .
- git commit -m "Update docs"
- git push --force --quiet "git@github.com:fbigun/fbigun.github.io.git" master:master
- cd ..
- hugo --baseURL //fbigun.coding.me/
- cd ./public
- git add -A .
- git commit --amend -m "Update docs"
- git push --force --quiet "git@git.coding.net:fbigun/fbigun.coding.me.git" master:master

notifications:
  email: false
```

## 文件参考引用

[git subtree插件](http://www.worldhello.net/gotgit/04-git-model/050-subtree-model.html#git-subtree)  
[使用Hugo搭建静态站点](http://tonybai.com/2015/09/23/intro-of-gohugo/)  
[Travis Ci的最接底气的中文使用教程](http://www.jianshu.com/p/8308b8f08de9)  
[Encryption keys](https://docs.travis-ci.com/user/encryption-keys/)  
[如何简单入门使用Travis-CI持续集成](https://github.com/nukc/how-to-use-travis-ci)  
[Hugo中文文档](http://www.gohugo.org/)
