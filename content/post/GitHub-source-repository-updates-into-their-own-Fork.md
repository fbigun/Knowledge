---
title: "GitHub将源仓库的更新合并到自己的Fork"
date: 2017-07-13T09:26:50+08:00
menu: "main"
Categories: ["Development","Github"]
Tags: ["Development","github"]
Description: "GitHub上有个很方便的功能叫Fork，可以将别人的工程一键复制到自己帐号下。"
---

# GitHub将源仓库的更新合并到自己的Fork

GitHub上有个很方便的功能叫Fork，可以将别人的工程一键复制到自己帐号下。这个功能很方便，但有点不足的是，当源项目更新后，你Fork的分支并不会一起更新，需要自己手动去更新。下面是其更新的方法：


>1、在本地装好GitHub客户端，或者Git客户端

>2、clone自己的fork分支到本地，可以直接使用github客户端，clone到本地，如果使用命令行，命令为：

~~~shell
git clone git@github.com:break123/three.js.git three.js
~~~

>3、增加源分支地址到你项目远程分支列表中(此处是关键)，命令为：

~~~shell
git remote add mrdoob git://github.com/mrdoob/three.js.git
~~~

此处可使用git remote -v查看远程分支列表

>4、fetch源分支的新版本到本地

~~~shell
git fetch mrdoob
~~~

>5、合并两个版本的代码

~~~shell
git merge mrdoob/master
~~~

>6、将合并后的代码push到GitHub上去

~~~shell
git push origin master
~~~
