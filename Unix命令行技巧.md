**为远程服务器快捷创建免密码登陆**
```shell
ssh-copy-id -i ~/.ssh/id_rsa.pub "-p port user@server"
```

**如果还没有密钥，请使用ssh-keygen命令生成。**
```shell
ssh-keygen -b 2048 -t rsa
ssh-keygen
```

**通过SSH连接屏幕**
```shell
ssh -t remote_host screen –r
```

直接连接到远程屏幕会话（节省了无用的父bash进程）。

**通过SSH运行复杂的远程shell命令**
```shell
ssh host -l user “`cat cmd.txt`”
```

**通过SSH将MySQL数据库复制到新服务器**
```shell
mysqldump –add-drop-table –extended-insert –force –log-error=error.log -uUSER -pPASS OLD_DB_NAME | ssh -C user@newhost “mysql -uUSER -pPASS NEW_DB_NAME”
```

通过压缩的SSH隧道Dump一个MySQL数据库，将其作为输入传递给mysql命令，我认为这是迁移数据>库到新服务器最快最好的方法。

**从一台没有SSH-COPY-ID命令的主机将你的SSH公钥复制到服务器**
```shell
cat ~/.ssh/id_rsa.pub | ssh user@machine “mkdir ~/.ssh; cat >> ~/.ssh/authorized_keys”`
```