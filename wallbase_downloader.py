#! /usr/bin/python
# coding=utf-8

# download wallpaper
# grab photos in [wallbase](http://wallbase.cc/)
# esp grab the photo must logging
# auth:stef.woo@gmail.com

import requests,os,time,re
from bs4 import BeautifulSoup
import cPickle as pickle
from sys import argv
from urlparse import urlparse
import lxml.html
from requests.auth import HTTPBasicAuth
import random

pickle_flie = os.path.join(os.path.dirname(__file__),'wallbase2.pkl')#给出文件的绝对地址
PAGE = 10
base_url = u'http://wallbase.cc/toplist/index/%s?purity=010'

# photo_url_dict = {}
# visited_idx = []

# user information
USER = "stefwoo"
PASSWORD = "Br1sjhhrhl"

# save path(must define)
# PATH = ""
# photo information
# SFW 100
# SKETCHY 010
# NSFW 001
# purity=['111','011','001']
# tags = ['boobs','pussy']


def init(pickle_flie,photo_url_dict = [],visited_idx = []):
	# 初始化，主要把字典和列表pickle到文件，这样通过pickle文件进行交互
	with open(pickle_flie, 'w') as f1:
		pickle.dump((photo_url_dict, visited_idx), f1)
	print "init is OK! You can grab NOW"

def wallbase_login():#login and return a session client
	login_url = u'http://wallbase.cc/user/login'
	client = requests.session() #create a session instance
	r = client.get(login_url) # sets cookie
	doc = lxml.html.document_fromstring(r.text)
	csrf = doc.xpath('//*[@id="logregform"]/form/input[1]/@value')[0] #catch csrf code
	payload = {'csrf':csrf,'ref':login_url,'username': USER, 'password': PASSWORD}
	client.post('http://wallbase.cc/user/do_login', data=payload)#login
	return client

def grab_url(base_url,pickle_flie,page,client):
	#抓取网页，获取图片编号和图片地址的关系，存入字典，如果已经下载，则不放入字典
	with open(pickle_flie) as f2:
		photo_url_dict, visited_idx = pickle.load(f2)

	for page in range(page):
		r = client.get(base_url%(page*32)).text
		doc = lxml.html.document_fromstring(r)
		for s in doc.xpath('//img/@data-original'):
			photo_url = str(s).replace('cc//','cc/').replace('thumbs','wallpapers').replace('thumb','wallpaper')
			if photo_url not in visited_idx:
				print photo_url
				photo_url_dict.append(photo_url)
				with open(pickle_flie, 'w') as f1:
					pickle.dump((photo_url_dict, visited_idx), f1)
		time.sleep(random.randint(8, 20))
		# for link in doc.find_all('img'):
		# s = link.get('data-original')
		# idx = re.search(r'\d+',photo_url).group()
	return grab_photo

def grab_photo(pickle_flie,client):
	# 传入一个photo的序号idx和一个图片的网址，然后进行下载并保存，文件名和idx一致
	with open(pickle_flie) as f3:
		photo_url_dict, visited_idx = pickle.load(f3)
	while photo_url_dict:
		photo_url =photo_url_dict.pop(0)
		with open(os.path.join("d:/010/",photo_url.split('/')[-1]), 'wb') as f:
			f.write(client.get(photo_url).content)
		print "photo %s has been downloaded!" % photo_url.split('/')[-1]
		visited_idx.append(photo_url)
		with open(pickle_flie, 'w') as f1:
			pickle.dump((photo_url_dict, visited_idx), f1)
		time.sleep(random.randint(12, 45))
	print "all photo in list download OK!"
	return grab_url

if __name__ == "__main__":
	# init(pickle_flie)
	# grab_url(base_url,pickle_flie,PAGE,client=wallbase_login())
	grab_photo(pickle_flie,client=wallbase_login())
	
	# script = argv
	# print "The script is called:", script
	# print "1: init;/t2: grab url;/t3: grab photo; "
	# print "Order must be 1>>>2>>>3"
	# print "please tape your chioce!"

	# chioce = raw_input('>')	

	# if chioce == '1': init(pickle_flie)
	# elif chioce == '2': grab_url(base_url,pickle_flie)
	# elif chioce == '3': grab_photo(pickle_flie)
	# else:print "chioce is empty!!!"




