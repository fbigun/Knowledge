---
date: "2016-12-24T17:01:47+08:00"
title: "Linux下FTP的配置文件的参数详解"
menu: "main"
Categories: ["Development","GoLang"]
Tags: ["Development","golang"]
Description: ""
---

Linux下FTP的配置文件的参数详解
---

`vsftpd`配置文件采用“#”作为注释符，以“#”开头的行和空白行在解析时将被忽略，其余的行被视为配置命令行，每个配置命令的“＝”两边不要留有**空格**。对于每个配置命令，在配置文件中还列出了相关的配置说明，利用vi编辑器可实现对配置文件的编辑修改。方法如下：
     #vi /etc/vsftpd/vsftpd.conf

1. 登录和对匿名用户的设置
`write_enable=YES`
//是否对登录用户开启写权限。属全局性设置。默认NO
`local_enable=YES`
//是否允许本地用户登录FTP服务器。默认为NO
`anonymous_enable=YES`
//设置是否允许匿名用户登录FTP服务器。默认为YES
`ftp_username=ftp`
//定义匿名用户的账户名称，默认值为ftp。
`no_anon_password=YES`
//匿名用户登录时是否询问口令。设置为YES，则不询问。默认NO
`anon_world_readable_only=YES`
//匿名用户是否允许下载可阅读的文档，默认为YES。
`anon_upload_enable=YES`
//是否允许匿名用户上传文件。只有在write_enable设置为YES时，该配置项才有效。而且匿名用户对相应的目录必须有写权限。默认为NO。
`anon_mkdir_write_enable=YES`
//是否允许匿名用户创建目录。只有在write_enable设置为    YES时有效。且匿名用户对上层目录有写入的权限。默认为NO。
`anon_other_write_enable=NO`
//若设置为YES，则匿名用户会被允许拥有多于上传和建立目录的权限，还会拥有删除和更名权限。默认值为NO。

2. 设置欢迎信息
用户登录FTP服务器成功后，服务器可向登录用户输出预设置的欢迎信息。
`ftpd_banner=Welcome to my FTP server.`
//该配置项用于设置比较简短的欢迎信息。若欢迎信息较多，则可使用banner_file配置项。
`banner_file=/etc/vsftpd/banner`
//设置用户登录时，将要显示输出的文件。该设置项将覆盖ftpd_banner的设置。
`dirmessage_enable=YES`
//设置是否显示目录消息。若设置为YES，则当用户进入特定目录（比如/var/ftp/linux）时，将显示该目录中的由message_file配置项指定的文件（.message）中的内容。
`message_file=.message`
//设置目录消息文件。可将显示信息存入该文件。该文件需要放在 相应的目录（比如/var/ftp/linux）下

3. 设置用户登录后所在的目录
`local_root=/var/ftp`
// 设置本地用户登录后所在的目录。默认配置文件中没有设置该项，此时用户登录FTP服务器后，所在的目录为该用户的主目录，对于root用户，则为/root目录。
`anon_root=/var/ftp`
//设置匿名用户登录后所在的目录。若未指定，则默认为/var/ftp目录。

4. 控制用户是否允许切换到上级目录
在默认配置下，用户可以使用`cd ..`命名切换到上级目录。比如，若用户登录后所在的目录为`/var/ftp`，则在“ftp&gt;”命令行下，执行`cd ..`命令后，用户将切换到其上级目录`/var`，若继续执行该命令，则可进入Linux系统的根目录，从而可以对整个Linux的文件系统进行操作。

若设置了`write_enable=YES`，则用户还可对根目录下的文件进行改写操作，会给系统带来极大的安全隐患，因此，必须防止用户切换到Linux的根目录，相关的配置项如下：
`chroot_list_enable=YES`
// 设置是否启用chroot_list_file配置项指定的用户列表文件。设置为YES则除了列在j/etc/vsftpd/chroot_list文件中的的帐号外，所有登录的用户都可以进入ftp根目录之外的目录。默认NO
`chroot_list_file=/etc/vsftpd/chroot_list`
// 用于指定用户列表文件，该文件用于控制哪些用户可以切换到FTP站点根目录的上级目录。
`chroot_local_user=YES`
// 用于指定用户列表文件中的用户，是否允许切换到上级目录。默认NO
注意：要对本地用户查看效果，需先设置`local_root=/var/ftp`

##具体情况有以下几种：
 1. 当`chroot_list_enable=YES`，`chroot_local_user=YES`时，在`/etc/vsftpd/chroot_list`文件中列出的用户，可以切换到上级目录；未在文件中列出的用户，不能切换到站点根目录的上级目录。
 2. 当`chroot_list_enable=YES`，`chroot_local_user=NO`时，在`/etc/vsftpd/chroot_list`文件中列出的用户，不能切换到站点根目录的上级目录；未在文件中列出的用户，可以切换到上级目录。
 3. 当`chroot_list_enable=NO`，`chroot_local_user=YES`时，所有用户均不能切换到上级目录。
 4. 当`chroot_list_enable=NO`，`chroot_local_user=NO`时，所有用户均可以切换到上级目录。
 5. 当用户不允许切换到上级目录时，登录后FTP站点的根目录`/`是该FTP账户的主目录，即文件的系统的`/var/ftp`目录。
