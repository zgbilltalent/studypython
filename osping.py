#!/usr/bin/python
# --*-- coding:utf-8 --*--

import os

list = ["taobao","jd","baidu","126","dinpay",""]#需要扫描的域名名称
i = 0
strlist = []#组装最后完整的网站域名
while list[i] != list[-1]:#不是列表list最后一个元素空格时，则进入
    str = "ping -c 5 www."#在linux系统中ping网站的域名的语法
    print str
    strlist.append(str+list[i]+".com")#组装成完整的域名
    os.system(strlist[i])#调用os模块进行ping操作
    i = i + 1