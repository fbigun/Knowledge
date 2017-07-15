---
title: "Goaccess依赖"
date: 2017-07-13T09:26:50+08:00
menu: "main"
Categories: ["Development","Goaccess"]
Tags: ["Development","Goaccess依赖"]
Description: "安装 Goaccess"
---

## Goaccess依赖

发行版|NCurses|NCurses Wide-Character|GLib >= 2.0.0|GeoIP (optional)
---|---|---|---|---  
Ubuntu/Debian|libncurses5-dev|libncursesw5-dev|libglib2.0-dev|libgeoip-dev
Fedora/RHEL/CentOS|ncurses-devel|ncurses-devel|glib2-devel|geoip-devel
Arch Linux|ncurses|ncurses|glib2|geoip
Gentoo|sys-libs/ncurses|sys-libs/ncurses|dev-libs/glib:2|dev-libs/geoip

## Debian/Ubuntu  系安装的方法  

```bash
# sudo su
$ echo "deb http://deb.goaccess.prosoftcorp.com $(lsb_release -cs) main" | tee -a /etc/apt/sources.list
$ wget -O - http://deb.goaccess.prosoftcorp.com/gnugpg.key | apt-key add -
$ apt-get update
su no-root-user
$ apt-get install goaccess
```

## 从源码安装  

```bash
$ wget http://downloads.sourceforge.net/project/goaccess/0.7.1/goaccess-0.7.1.tar.gz
$ tar -xzvf goaccess-0.7.1.tar.gz
$ cd goaccess-0.7.1/
$ ./configure --enable-geoip --enable-utf8
$ make
# make install
```

## Git Clone 安装  

```bash
$ git clone https://github.com/allinurl/goaccess.git
$ cd goaccess
$ autoreconf -fi
$ ./configure --enable-geoip --enable-utf8
$ make
# make install
```
##FAQ

1. 输入命令后，出现 `goaccess Error Opening file /usr/share/GeoIP/GeoIP.dat`或安装完成后未配置.goaccessrc,输入命令`goaccess -f access.log`选完输出格式后无反应。
A：一般可能是没有安装Geoip-data.dat。运行命令`sudo apt-get install geoip-datebase`
