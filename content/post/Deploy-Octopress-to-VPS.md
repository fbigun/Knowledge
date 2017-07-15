---
date: "2016-12-24T17:01:47+08:00"
title: "部署 Octopress 到 VPS"
menu: "main"
Categories: ["Development","博客"]
Tags: ["Development","golang"]
Description: "Octopress官方已经提供三种方法来部署博客,Github Pages、Heroku 和 使用 Rsync 命令来同步博客,今天我来介绍如何利用 git 将 Octopress 自动部署部署到 VPS 上，我的线上环境 Linode VPS，用的是 Debian 6，本地是用的 os x。"
---

# 部署 Octopress 到 VPS

Octopress官方已经提供三种方法来部署博客,Github Pages、Heroku 和 使用 Rsync 命令来同步博客,今天我来介绍如何利用 git 将 Octopress 自动部署部署到 VPS 上，我的线上环境 Linode VPS，用的是 Debian 6，本地是用的 os x。

**推荐一些扩展阅读:**

>[Pro Git](http://git-scm.com/book/zh/) \[墙\]

>[Pro Git on Github](https://github.com/progit/progit)

### 安装 Git

**在 Debian 上安装**

~~~shell
apt-get install git
~~~

### 使用 Git

**第一次运行设置**

~~~shell
git config --global user.name "Your Name"
git config --global user.email your.email@example.com
git config --global alias.co checkout  //设置checkout替代命令
git config --global core.editor "vim -f"  //设置编辑器
~~~

### 线上 VPS 配置

打开终端，SSH 连接 VPS

~~~shell
ssh root@www.squidv.com
~~~

新建一个 git 用户

~~~shell
adduser git --ingroup sudo  // 新建 git 用户并将其加入到root组
su git  // 进入 git 用户
cd  // 返回根目录
~~~

创建一个裸仓库

~~~shell
mkdir octopress.git && cd octopress.git
~~~

初始化一个空的 git 仓库–shared 可以指定其他行为，只是默认为将组权限改为可写并执行 g+sx，所以最后会得到 rws

~~~shell
sudo git init --bare --shared
cd hooks
sudo wget https://gist.github.com/cpennlee/5458728/raw/e39dc0ccf0d0ed160aa45c30c62a28e35dcba580/post-receive.sh
sudo chmod 755 post-receive // 变更权限使其可执行
sudo vim post-receive // 更改你的博客要存储的 WEB 文件目录
:x //保存并退出
~~~

我们把octopress.git的目录指向web文件目录，当我们从本地push的文件，就能自动 checkout 到web文件目录了。

我们还需要配置 nginx 安装参考 [部署 Ruby on Rails 到 VPS 使用 Nginx MySQL Unicorn](http://squidv.com/deploying-ruby-on-rails/)

~~~shell
sudo touch /etc/nginx/sites-available/blog.squidv.com
~~~

blog.squidv.com
~~~
server {
  # 域名绑定
  server_name blog.squidv.com;

  # 本地目录
  root /home/deployer/blog;

  # 设置默认页面
  index index.html;

  autoindex off;

  # 定义根目录
  location / {
try_files $uri $uri/ =404;
  }

  location ~ /\. {
      access_log off;
      log_not_found off;
      deny all;
  }

  location ~ ~$ {
      access_log off;
      log_not_found off;
      deny all;
  }

  location = /robots.txt {
      access_log off;
      log_not_found off;
  }

  location = /favicon.ico {
      access_log off;
      log_not_found off;
  }
}
~~~

~~~shell
sudo ln -s /etc/nginx/sites-available/blog.squidv.com /etc/nginx/sites-enabled/blog.squidv.com // 关联文件
sudo /etc/init.d/nginx reload // 重新启动 nginx
~~~

### 本地操作

~~~shell
git clone git://github.com/imathis/octopress.git  // 获取octopress 源码
cd octopress
git remote add origin ssh://root@blog.squidv.com/home/git/octopress.git
git push origin +master:refs/heads/master
~~~

OK! 成功同步到VPS上.
