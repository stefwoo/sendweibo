#! /usr/bin/python
#coding=utf-8

from weibo_request import Client
import smtplib, time
from email.mime.text import MIMEText
# import sys
import os

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


token_file = 'token_file.log'
since_id_file = 'since_id.log'
abs_path = os.path.dirname(__file__)


APP_KEY = '1021805059' # app key
APP_SECRET = 'fc6af22b6147925b79c08ad5adfee78c' # app secret
CALL_BACK = 'https://api.weibo.com/oauth2/default.html' # callback url
UID = [1698194380, 1038819010, 1732523361]

def run():
	f1 = open(os.path.join(abs_path, token_file))
	saved_token = eval(f1.read())
	f1.close()

	f2 = open(os.path.join(abs_path, since_id_file))
	since_id = int(f2.read())
	f2.close()

	client = Client(APP_KEY, APP_SECRET, CALL_BACK, saved_token)


	print since_id
	loop = 1

	while True:
		res = client.get('statuses/home_timeline',since_id=since_id)
		print type(res)
		# print res['hasvisible']
		for i in res['statuses']:
			# print type(i)
			if i['user']['id'] in UID:
				msg = i['user']['screen_name']+">>>"+i['text']
				send_mail(mailto_list,i['user']['screen_name']+" has a new blog",msg.encode('utf-8'))

				since_id = i['id']
				# print since_id
				f3 = open(os.path.join(abs_path, since_id_file),'w')
				f3.truncate()
				f3.write(str(since_id))
				f3.close()
		print "Loop  : %d, Time : %s , since_id : %d " % (loop, str(time.ctime()), since_id)
		loop += 1
		time.sleep(60)

	# client.post('statuses/update', status='python sdk test')


def get_tk():
	c = Client(APP_KEY, APP_SECRET, CALL_BACK)
	print c.authorize_url
	code = raw_input('please paste code here')
	c.set_code(code)
	print str(c.token)
	import os
	f = open(os.path.join(abs_path, token_file),'w')
	f.write(str(c.token))
	f.close()
	# f = eval(i.read())

if __name__ == "__main__":
	run()
	# get_tk()

