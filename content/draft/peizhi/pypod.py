#!/usr/bin/env python
#-*- coding:utf-8 -*-
 
import httplib, urllib
import socket
import time
 
params = dict(
    login_email="rsdhlz@qq.com", # replace with your email
    login_password="hyan1314", # replace with your password
    format="json",
    domain_id=23070278, # replace with your domain_od, can get it by API Domain.List
    record_id=105982520, # replace with your record_id, can get it by API Record.List
    sub_domain="www", # replace with your sub_domain
    record_line="默认",
)
current_ip = None
 
def ddns(ip):
    params.update(dict(value=ip))
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/json"}
    conn = httplib.HTTPSConnection("dnsapi.cn")
    conn.request("POST", "/Record.Ddns", urllib.urlencode(params), headers)
     
    response = conn.getresponse()
    print response.status, response.reason
    data = response.read()
    print data
    conn.close()
    return response.status == 200
 
def getip():
    sock = socket.create_connection(('ns1.dnspod.net', 6666))
    ip = sock.recv(16)
    sock.close()
    return ip
 
if __name__ == '__main__':
    while True:
        try:
            ip = getip()
            print ip
            if current_ip != ip:
                if ddns(ip):
                    current_ip = ip
        except Exception, e:
            print e
            pass
        time.sleep(30)
