#!/usr/bin/env python
2  # -*- coding:utf-8 -*- 
3  #Author: xiaomoren
# @Time    : 2018/2/12 15:59
import itchat,time
import requests
from webpage_to_iChat.jieping import  capture

itchat.auto_login(hotReload=True)
i = 0
while True:
    url = 'www.xxx.com'
    a = requests.get(url)
    capture(url, save_fn='test.png')
    if a.status_code == 200:
        user = itchat.search_friends(name=u'xxx')[0]
        user.send("@img@%s" % 'test.png')
        user.send('状态码为：%d'% a.status_code,'返回长度为：')
        time.sleep(5)

