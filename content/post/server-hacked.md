---
title: "检查服务器入侵简略指南"
date: 2017-12-07T12:57:50+08:00
menu: "main"
Categories: ["Development"]
Tags: ["Development","服务器", "安全"]
Description: "检查服务器入侵简略指南"
---

# 检查服务器入侵简略指南

## 当前都有谁登录

```bash
w
whois

# 两个命令都能查询当前登录用户
```

## 都有谁曾经登录

```bash
last

# 记录登录历史的文件
# /var/log/wtmp
```

## 命令历史记录

```bash
history

# 记录命令历史的文件
# ./bash_history
```

## 大量消耗CPU资源进程

```
top
# 查看消耗资源的进程 PID

strace -p PID
lsof -p PID
# 查看PID进程正在使用的系统资源
```

## 查看系统所有运行的进程

```bash
ps auxf
```

## 检查进程使用网络的情况

```bash
iftop
```

## 检查网络监听链接

```bash
lsof -i
netstat -plunt
```

> 特别需要留意的时处于 LISTEN ENTABLISHED 两种状态的链接
> 使用 lsof、 strace 命令查看进程行为

## 察觉到入侵后配置和应用防火墙并杀死相关的 ssh 会话

```bash
iptables YOU_IP ACCEPT
iptables * DROP
kill -9 PID
```
