#! /usr/bin/python
# coding=utf-8

from initclient import initclient
import smtplib, time
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
    msg = MIMEText(content)
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

APP_KEY = '1021805059' # app key
APP_SECRET = 'fc6af22b6147925b79c08ad5adfee78c' # app secret
CALL_BACK = 'https://api.weibo.com/oauth2/default.html' # callback url

def run():
		#调用initclietn模块创建授权的client对象
	client = initclient.get_client(APP_KEY, APP_SECRET, CALL_BACK)
	if not client:
			return

	UID = [1698194380, 1038819010, 1732523361, ]
	since_id = 0
	loop = 1
	while True:
		r = []
		r = client.statuses.friends_timeline.get(since_id = since_id)
		if r.statuses:
			since_id = r.statuses[0].id
			for message in r.statuses:
				if message.user.id in UID:
					# print message.text.encode()
					msg = message.user.screen_name+":"+message.text
					# print type(msg)
					send_mail(mailto_list,message.user.screen_name+" has a new blog",msg.encode('gb2312'))
		print "Loop  : %d, Time : %s , since_id : %d " % (loop, str(time.ctime()), since_id)
		loop = loop + 1
		time.sleep(60)
		
if __name__ == "__main__":
	run()
