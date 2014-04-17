#手工打造干净精简的Debian VPS系统#

买VPS回来，一般提供商安装的系统都是自带apache神马一大堆乱七八糟玩意，占硬盘占内存不说，一不小心冲突起来挂档神马的。那就是欲哭无泪啦。所以，本大人……

本小菜手工把Debian的标准版和迷你版对比，将所有多余程序卸载！

*如果不想看原理只想一步到位，请跳到文章最后：*

注意，以下星号是为了一起卸载有关组件、减少垃圾；

##多余的服务类软件（会自己启动，影响较大的）：##

~~~
**以下为引用的内容：**
apache2-* //apache服务器，我们一般自己重装或者换Nginx等等
bind9-* //dns服务器，我们一般不在自己VPS上搭建DNS服务器，果断卸掉
xinetd //xinetd是服务守护进程，比如平时ftp服务器未开启，发现有人访问21端口则自动启动ftp服务器。VPS不需要
samba-* //samba能让linux系统使用windows的共享功能，VPS显然不需要
nscd-* //DNS缓存软件，同bind9，不需要
portmap //端口转发，一般Web服务器不需要
sendmail-* //发送邮件用，一般程序都使用php-sendmail，不需要这个
sasl2-bin //一个权限程序，不光占用资源，还容易在建立系统账户时候出错，果断删掉
~~~

##多余的系统组件（不会自启动，但是占用硬盘，也许还会造成冲突什么的）：##

~~~
以下为引用的内容：
lynx //文本浏览器，一般人系用不到滴~~
memtester //测试内存有没有坏，我没那么无聊……
unixodbc odbcinst-* //odbc数据库，主要给windows用，做网站一般用不到
python-* //大名鼎鼎的Python语言，如果正常玩linux很可能用到，但是Web服务器是用不到的
sudo //让授权过的普通用户获得root权限，VPS不需要
tcpdump //TCP抓包，你用么？
ttf-* //桌面环境用的字体，我们只要命令行……
~~~

##可以更换的系统组件：##

~~~
以下为引用的内容：
ksyslog或rsyslog -> inetutils-syslogd //这是系统日志，前两者功能齐全，但是系统占用就多余了（其实都不装也可以）
vim-* -> nano //vim编辑器大名鼎鼎，可是我真的不会用，而且虽然资源比emacs小了若干，还是拼不过nano……
bash -> dash或pdksh //bash控制台也有点臃肿了，不过为了方便，不是必要不用换掉。
openssh -> dropbear //这是SSH服务端，如果你喜欢在SSH上开一堆账号给人Fan Q的话，还是换了吧，有了Dropbear，每个SSH能省好几M内存呢。
~~~

##我们把所有操作写成脚本：##

###首先，系统升级：###

~~~shell
apt-get update&&apt-get upgrade
~~~

###完全多余的软件:###

~~~shell
apt-get -y purge apache2-* bind9-* xinetd samba-* nscd-* portmap sendmail-* sasl2-bin
~~~

###多余的系统组件###

~~~shell
apt-get -y purge lynx memtester unixodbc python-* odbcinst-* sudo tcpdump ttf-*
~~~

###替换的软件，请自行考虑选择并替换。###

##最后，记得清理一下：##

~~~shell
apt-get autoremove && apt-get clean
~~~

##再次更新系统##

~~~shell
apt-get update&&apt-get upgrade
~~~

贴出优化成果示例

~~~
以下为引用的内容：
root@bvm1:~# ps -A
PID TTY TIME CMD
1 ? 00:00:00 init
1433 ? 00:00:00 syslogd
1457 ? 00:00:00 cron
1463 ? 00:00:00 sshd
1485 ? 00:00:00 sshd
1504 pts/0 00:00:00 bash
3139 pts/0 00:00:00 ps
root@bvm1:~# free -m
total used free shared buffers cached
Mem: 256 10 245 0 0 0
-/+ buffers/cache: 10 245
Swap: 0 0 0
~~~
