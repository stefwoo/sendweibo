#! /usr/bin/python
#coding=utf-8

import smtplib
from email.mime.text import MIMEText

# 这段主要是设置邮件的收发
mailto_list=["stef.woo@gmail.com",]
mail_host="smtp.126.com"
mail_user="weibochecker"
mail_pass="newweibocoming!"
mail_postfix="126.com"
def send_mail(to_list,sub,content):
    '''
    to_list:发给谁
    sub:主题
    content:内容
    send_mail("aaa@126.com","sub","content")
    '''
    me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,'html','utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e), time.ctime()
        return False

if __name__ == "__main__":
	# run()
	# get_tk()
	s=u'<html><h4>主贴：</h4><p>明年夏天前我要成为这样。</p><h4>图片：</h4><img src="" /><h4>转发：</h4><p>只要坚持努力，我们都会成为自己心目中的明星。今天你锻炼了吗？</p><h4>转发的图片:</h4><img src="http://ww3.sinaimg.cn/large/c0534be6jw1e9gcnx0zf6j20dw0nu76a.jpg" /></html>'
	send_mail(mailto_list,"someone has a new blog",s)

