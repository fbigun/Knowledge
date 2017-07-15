#!/bin/sh
#@author:router_mail@163.com

thunderpath=/thunderembed
test -x $thunderpath/portal || exit

################################### excute ########################################################
cut -d: -f1 /etc/passwd|grep -q thunder || useradd --no-create-home --user-group --shell /bin/bash thunder

if [ $# -eq 0 ];then
    su - thunder -c $thunderpath/portal
elif [ $1 = "-s" ];then
    $thunderpath/portal -s
elif [ $1 = "-S" ];then
    $thunderpath/portal -s
else
    echo "Usage: thunder [-s]"
    echo "               -s         stop service, if given, other options are ignored"
    echo "               -h         show this help message"
fi
