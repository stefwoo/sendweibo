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
        print 'One email has been sent!'
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
UID = [1698194380, 1038819010,1662047260,1850235592]

def run():
	f1 = open(os.path.join(abs_path, token_file))
	saved_token = eval(f1.read())
	f1.close()#读取token，其实可以用pickle

	f2 = open(os.path.join(abs_path, since_id_file))
	since_id = int(f2.read())
	f2.close()#读取崩溃前的抓取记录print since_id

	client = Client(APP_KEY, APP_SECRET, CALL_BACK, saved_token)# client.post('statuses/update', status='python sdk test')#发微博示例
	loop = 1
	while True:
		res = client.get('statuses/home_timeline',since_id=since_id)# print type(res)# print res['hasvisible']
		for i in res['statuses']:# statuses是一个列表，列表里面的每个元素是字典
			if i['user']['id'] in UID:
				user_msg = i['user']['screen_name']+">>>"+i['text']#格式：user>>>说了什么话
				original_pic_url = i.get('original_pic','')#如果配图返回图片地址，否则返回空格
				retweeted_status_text = i.get('retweeted_status',{}).get('text','')#如果retweet则返回retweet的text,否则返回空格
				retweeted_statusc_pic = i.get('retweeted_status',{}).get('original_pic','')#如果retweet配图则返回图片地址，否则返回空格
				msg = u'<html><h4>主贴：</h4><p>%s</p><h4>图片：</h4><img src="%s" /><h4>转发：</h4><p>%s</p><h4>转发的图片:</h4><img src="%s" /></html>' \
				% (user_msg, original_pic_url, retweeted_status_text,retweeted_statusc_pic)#构建一个html，把所有的信息包括进去
				print msg.encode('utf-8')
				send_mail(mailto_list,i['user']['screen_name']+" has a new blog",msg)
				since_id = i['id']# print since_id
				f3 = open(os.path.join(abs_path, since_id_file),'w')
				f3.truncate()
				f3.write(str(since_id))
				f3.close()
				break
		print "Loop  : %d, Time : %s , since_id : %d " % (loop, str(time.ctime()), since_id)
		loop += 1
		time.sleep(60)

def get_tk():#获取令牌
	c = Client(APP_KEY, APP_SECRET, CALL_BACK)
	print c.authorize_url
	code = raw_input('please paste code here')
	c.set_code(code)
	print str(c.token)
	import os
	f = open(os.path.join(abs_path, token_file),'w')
	f.write(str(c.token))
	f.close()

if __name__ == "__main__":
	run()
	# get_tk()#获取令牌

	# 报错信息：
	# Loop  : 1, 29次
	# Errno 27次
	# Traceback 35次
	# Max retries exceeded with url 25次
 # 	EOF occurred in violation of protocol 10次

