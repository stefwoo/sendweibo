#! /usr/bin/python
#coding=utf-8

# import urllib2
# import socket

# class MyException(Exception):
#     pass

# try:
# 	print "first"
# 	urllib2.urlopen("http://twitter.com", timeout = 1)
# # help(urllib2)
# # urllib2.urlopen("http://www.baidu.com",timeout = 1)
# # urllib2.urlopen()
# except urllib2.URLError, e:
#     # print e
#     print "second"
#     if isinstance(e.reason, socket.timeout):
#         raise MyException("There was an error: %r" % e)
#     else:
#         # reraise the original error
#         raise
# # print "hello world"
import time
boundary = '----------%s' % hex(int(time.time() * 1000))
print time.time()
print time.time()*1000
print boundary


i = "i am sorry!"
print 'sors' in i


print i.replace('sorry', 'happy')


# import smtplib, time
# from email.mime.text import MIMEText

# mailto_list=["stef.woo@gmail.com",]
# mail_host="smtp.126.com"
# mail_user="weibochecker"
# mail_pass="newweibocoming!"
# mail_postfix="126.com"
# def send_mail(to_list,sub,content):
#     '''
#     to_list:发给谁
#     sub:主题
#     content:内容
#     send_mail("aaa@126.com","sub","content")
#     '''
#     me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
#     msg = MIMEText(content)
#     msg['Subject'] = sub
#     msg['From'] = me
#     msg['To'] = ";".join(to_list)
#     s = smtplib.SMTP()
#     s.connect(mail_host)
#     s.login(mail_user,mail_pass)
#     s.sendmail(me, to_list, msg.as_string())
#     s.close()
#     return True

# send_mail(mailto_list,"test in python",'here is in home')

