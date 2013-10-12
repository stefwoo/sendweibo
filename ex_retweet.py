#! /usr/bin/python
#coding=utf-8
s=u'''
{
			"created_at": "Thu Oct 10 21:23:22 +0800 2013",
			"id": 3631965029036425,
			"mid": "3631965029036425",
			"idstr": "3631965029036425",
			"text": "明年夏天前我要成为这样。",
			"source": "<a href=http://app.weibo.com/t/feed/c66T5g rel=nofollow>Android客户端</a>",
			"in_reply_to_status_id": "",
			"in_reply_to_user_id": "",
			"in_reply_to_screen_name": "",
			"pic_urls": [],
			"user": {
				"id": 1400512763,
				"idstr": "1400512763",
				"class": 1,
				"screen_name": "老摇啊摇",
				"name": "老摇啊摇",
				"province": "51",
				"city": "1",
				"location": "四川 成都",
				"description": "民谣。诗。街头表演。独立内敛百折不挠。",
				"url": "",
				"profile_image_url": "http://tp4.sinaimg.cn/1400512763/50/5670727073/1",
				"profile_url": "u/1400512763",
				"domain": "",
				"weihao": "",
				"gender": "m",
				"followers_count": 99,
				"friends_count": 69,
				"statuses_count": 1636,
				"favourites_count": 13,
				"created_at": "Sun Mar 11 09:49:24 +0800 2012",
				"verified_type": -1,
				"remark": "",
				"ptype": 0,
				"avatar_large": "http://tp4.sinaimg.cn/1400512763/180/5670727073/1",
				"avatar_hd": "http://ww2.sinaimg.cn/crop.81.0.477.477.1024/537a20fbjw8e7cs3bskt0j20hs0d9q3q.jpg",
				"verified_reason": "",
				"online_status": 1,
				"bi_followers_count": 41,
				"lang": "zh-cn",
				"star": 0,
				"mbtype": 0,
				"mbrank": 0,
				"block_word": 0
			},
			"retweeted_status": {
				"created_at": "Thu Oct 10 20:18:45 +0800 2013",
				"id": 3631948759065236,
				"mid": "3631948759065236",
				"idstr": "3631948759065236",
				"text": "只要坚持努力，我们都会成为自己心目中的明星。今天你锻炼了吗？",
				"source": "<a href=http://app.weibo.com/t/feed/3KeSKPrel=nofollow>WeicoPro</a>",
				"in_reply_to_status_id": "",
				"in_reply_to_user_id": "",
				"in_reply_to_screen_name": "",
				"pic_urls": [
					{
						"thumbnail_pic": "http://ww3.sinaimg.cn/thumbnail/c0534be6jw1e9gcnx0zf6j20dw0nu76a.jpg"
					}
				],
				"thumbnail_pic": "http://ww3.sinaimg.cn/thumbnail/c0534be6jw1e9gcnx0zf6j20dw0nu76a.jpg",
				"bmiddle_pic": "http://ww3.sinaimg.cn/bmiddle/c0534be6jw1e9gcnx0zf6j20dw0nu76a.jpg",
				"original_pic": "http://ww3.sinaimg.cn/large/c0534be6jw1e9gcnx0zf6j20dw0nu76a.jpg",
				"user": {
					"id": 3226684390,
					"idstr": "3226684390",
					"class": 1,
					"screen_name": "健身圣经",
					"name": "健身圣经",
					"province": "400",
					"city": "16",
					"location": "海外 其他",
					"description": "健康生活，身体强健，增强自信。",
					"url": "",
					"profile_image_url": "http://tp3.sinaimg.cn/3226684390/50/40023306744/1",
					"profile_url": "u/3226684390",
					"domain": "",
					"weihao": "",
					"gender": "m",
					"followers_count": 62958,
					"friends_count": 2270,
					"statuses_count": 3020,
					"favourites_count": 0,
					"created_at": "Tue Mar 19 10:35:21 +0800 2013",
					"verified_type": -1,
					"remark": "",
					"ptype": 0,
					"avatar_large": "http://tp3.sinaimg.cn/3226684390/180/40023306744/1",
					"avatar_hd": "http://tp3.sinaimg.cn/3226684390/180/40023306744/1",
					"verified_reason": "",
					"online_status": 0,
					"bi_followers_count": 275,
					"lang": "zh-cn",
					"star": 0,
					"mbtype": 12,
					"mbrank": 3,
					"block_word": 0
				},
				"reposts_count": 35,
				"comments_count": 13,
				"attitudes_count": 9,
				"mlevel": 0,
				"visible": {
					"type": 0,
					"list_id": 0
				}
			},
			"annotations": [
				{
					"client_mblogid": "69877ff5-e8cb-46dd-a4fb-8b08e536feaf"
				}
			],
			"reposts_count": 0,
			"comments_count": 0,
			"attitudes_count": 0,
			"mlevel": 0,
			"visible": {
				"type": 0,
				"list_id": 0
			}
		}
'''
# import json
# s2 = json.dumps(s)
# json1 = json.loads(s2)
# print type(s)
# print type(json1)
# print json1['text'].encode('utf-8')
dict1 = eval(s)
print type(dict1)
s1 = dict1.get('retweeted_status',{}).get('text','')
s2 = dict1.get('retweeted_status',{}).get('original_pic','')
s3 = dict1.get('text')
print s1 ,s2 ,s3
# u1 = unicode(s1)
# u2 = unicode(s2)
# u3 = unicode(s3)
# print u1,u2,u3

msg1 = '<html><h4>主贴：</h4><p>%s</p><h4>图片：</h4><img src="" /><h4>转发：</h4><p>%s</p><h4>转发的图片:</h4><img src="%s" /></html>' % (s3,s1,s2)

print msg1#.encode('gb2312')


import smtplib  
from email.mime.text import MIMEText  
  
sender = 'weibochecker@126.com'  
receiver = 'stef.woo@gmail.com'  
subject = 'python email test'  
smtpserver = 'smtp.126.com'  
username = 'weibochecker'  
password = 'newweibocoming'  

# mailto_list=["stef.woo@gmail.com",]
# mail_host="smtp.126.com"
# mail_user="weibochecker"
# mail_pass="newweibocoming!"
# mail_postfix="126.com"
 
msg = MIMEText(msg1,'html','utf-8')  
 
msg['Subject'] = subject  

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()

# <h4>主贴：</h4><p>明年夏天前我要成为这样。</p><h4>图片：</h4><img src="" /><h4>转发：</h4><p>只要坚持努力，我们都会成为自己心目中的明星。今天你锻炼了吗？</p><h4>转发的图片:</h4><img src="http://ww3.sinaimg.cn/large/c0534be6jw1e9gcnx0zf6j20dw0nu76a.jpg" alt="Inline image 1" />

# <img src="http://ww3.sinaimg.cn/large/c0534be6jw1e9gcnx0zf6j20dw0nu76a.jpg" alt="Inline image 1">





# {
# 			"created_at": "Thu Oct 10 21:29:09 +0800 2013",
# 			"id": 3631966475433494,
# 			"mid": "3631966475433494",
# 			"idstr": "3631966475433494",
# 			"text": "【河北证实男子自锯右腿：正为其申请下半年救助金】河北清苑县官员今日下午证实，村民郑艳良患怪病自锯右腿属实，“主要是因为他患病后疼痛难忍，医院诊断治不了。”该官员称，郑今年上半年政府为郑艳良发放5000元的救助金，现正申请下半年救助金，村里也正为他协调申请装假肢。http://t.cn/zRbNGlk",
# 			"source": "<a href=\"http://weibo.com/\" rel=\"nofollow\">新浪微博</a>",
# 			"favorited": false,
# 			"truncated": false,
# 			"in_reply_to_status_id": "",
# 			"in_reply_to_user_id": "",
# 			"in_reply_to_screen_name": "",
# 			"pic_urls": [
# 				{
# 					"thumbnail_pic": "http://ww2.sinaimg.cn/thumbnail/60718250jw1e9gep0mj92j20a00dct9i.jpg"
# 				}
# 			],
# 			"thumbnail_pic": "http://ww2.sinaimg.cn/thumbnail/60718250jw1e9gep0mj92j20a00dct9i.jpg",
# 			"bmiddle_pic": "http://ww2.sinaimg.cn/bmiddle/60718250jw1e9gep0mj92j20a00dct9i.jpg",
# 			"original_pic": "http://ww2.sinaimg.cn/large/60718250jw1e9gep0mj92j20a00dct9i.jpg",
# 			"geo": null,
# 			"user": {
# 				"id": 1618051664,
# 				"idstr": "1618051664",
# 				"class": 1,
# 				"screen_name": "头条新闻",
# 				"name": "头条新闻",
# 				"province": "11",
# 				"city": "8",
# 				"location": "北京 海淀区",
# 				"description": "每日播报全球各类重要资讯、突发新闻，全天24小时即时发布。欢迎报料、投稿，请发私信或者邮件：xlttnews@vip.sina.com。",
# 				"url": "http://news.sina.com.cn/",
# 				"profile_image_url": "http://tp1.sinaimg.cn/1618051664/50/5661558324/0",
# 				"profile_url": "breakingnews",
# 				"domain": "breakingnews",
# 				"weihao": "",
# 				"gender": "f",
# 				"followers_count": 22899318,
# 				"friends_count": 194,
# 				"statuses_count": 77291,
# 				"favourites_count": 7,
# 				"created_at": "Fri Aug 28 16:34:36 +0800 2009",
# 				"following": true,
# 				"allow_all_act_msg": true,
# 				"geo_enabled": true,
# 				"verified": true,
# 				"verified_type": 3,
# 				"remark": "",
# 				"ptype": 0,
# 				"allow_all_comment": true,
# 				"avatar_large": "http://tp1.sinaimg.cn/1618051664/180/5661558324/0",
# 				"avatar_hd": "http://tp1.sinaimg.cn/1618051664/180/5661558324/0",
# 				"verified_reason": "新浪新闻中心24小时播报全球重大新闻",
# 				"follow_me": false,
# 				"online_status": 1,
# 				"bi_followers_count": 172,
# 				"lang": "zh-cn",
# 				"star": 0,
# 				"mbtype": 0,
# 				"mbrank": 0,
# 				"block_word": 0
# 			},
# 			"reposts_count": 215,
# 			"comments_count": 226,
# 			"attitudes_count": 68,
# 			"mlevel": 0,
# 			"visible": {
# 				"type": 0,
# 				"list_id": 0
# 			}
# 		},