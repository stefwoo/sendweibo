#! /usr/bin/python
#coding=utf-8
# import urllib,urlparse,re
# def rpb(blocknum, blocksize, totalsize):
#     percent = 100.0 * blocknum * blocksize / totalsize
#     if percent > 100:percent = 100
#     print "%.2f%%"% percent

# # # urllib.urlretrieve("http://ww4.sinaimg.cn/bmiddle/65c77184jw1e9innq5vkzj20dc0hsac3.jpg", 'd:/11.png')
# # s = urlparse.urlparse('http://ww4.sinaimg.cn/bmiddle/65c77184jw1e9innq5vkzj20dc0hsac3.jpg')[2]
# # print re.search('/(.*.jpg)', s).group()

# s1 = 'http://ww4.sinaimg.cn/bmiddle/65c77184jw1e9innq5vkzj20dc0hsac3.jpg'
# print s1.split('/')[-1]


# import requests

# with open('d:/wallpaper-3032835-3.png', 'wb') as f:
# 	f.write(requests.get("http://wallpapers.wallbase.cc/rozne/wallpaper-3032835.png").content)


base_url = u'http://wallbase.cc/search?purity=001'
# login_url = u'http://wallbase.cc/user/login'
USER = "stef.woo@gmail.com"
PASSWORD = "Br1sjhhrhl"
from requests.auth import HTTPBasicAuth
page = requests.get(base_url, auth=HTTPBasicAuth(USER, PASSWORD)).text #login
doc = lxml.html.document_fromstring(page)
for s in doc.xpath('//img/@data-original'):
# for link in doc.find_all('img'):
# 	s = link.get('data-original')
	photo_url = str(s).replace('cc//','cc/').replace('thumbs','wallpapers').replace('thumb','wallpaper')
	print photo_url
