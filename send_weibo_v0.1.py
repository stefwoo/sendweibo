#! /usr/bin/python
#coding=utf-8

from initclient import initclient
import smtplib, time
from email.mime.text import MIMEText
import sys

mailto_list=["stef.woo@gmail.com",]
mail_host="smtp.126.com"
mail_user="weibochercker"
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
    # try:
    s = smtplib.SMTP()
    s.connect(mail_host)
    s.login(mail_user,mail_pass)
    s.sendmail(me, to_list, msg.as_string())
    s.close()
    return True
    # except Exception, e:
    #     print str(e), time.ctime()
    #     return False

APP_KEY = '1021805059' # app key
APP_SECRET = 'fc6af22b6147925b79c08ad5adfee78c' # app secret
CALL_BACK = 'https://api.weibo.com/oauth2/default.html' # callback url

def run():
		#调用initclietn模块创建授权的client对象
	client = initclient.get_client(APP_KEY, APP_SECRET, CALL_BACK)
	if not client:
			return

	UID = [1698194380, 1038819010] #ffice weibo stefwoo=1038819010
	since_id = 0 # message which is catch  must late than since_id 
	# message_id = 0
	#COUNT = 10 #count is the max of message
	loop = 1
	while True:
		r = []
		# try:
		r = client.statuses.friends_timeline.get(trim_user = 1, since_id = since_id)
        #, count = COUNT)
		if r.statuses:
			since_id = r.statuses[0].id
			for message in r.statuses:
				if message.uid in UID:# and (message.id > message_id):
					# try:
					send_mail(mailto_list,"weibo has a new blog",message.text.encode('gb2312'))
					print "A new message found!"
					# except:
						# print "send mail failed : ", sys.exc_info()
					break            
		# except:
		# 	print "Unexpected error:", sys.exc_info()
		print "Loop  : %d, Time : %s , since_id : %d " % (loop, str(time.ctime()), since_id)
		loop = loop + 1
		time.sleep(60)

#		#根据用户输入内容发微博
#	while True:
#		print "Ready! Do you want to send a new weibo?(y/n)"
#		choice = raw_input()
#		if choice == 'y' or choice == 'Y':
#			content = raw_input('input the your new weibo content : ')
#			if content:
#				client.statuses.update.post(status=content)
#				print "Send succesfully!"
#				break;
#			else:
#				print "Error! Empty content!"
#		if choice == 'n' or choice == 'N':
#			print "Goodbye!"
#			break
#

if __name__ == "__main__":
	run()
