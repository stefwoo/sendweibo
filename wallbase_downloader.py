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
# from requests.auth import HTTPBasicAuth

pickle_flie = os.path.join(os.path.dirname(__file__),'wallbase.pkl')#给出文件的绝对地址
base_url = u'http://wallbase.cc/search?purity=100'
# photo_url_dict = {}
# visited_idx = []

# user information
# USER = ""
# PASSWORD = ""

# save path(must define)
# PATH = ""
# photo information
# SFW 100
# SKETCHY 010
# NSFW 001
# purity=['111','011','001']
# tags = ['boobs','pussy']


def init(pickle_flie,photo_url_dict = {},visited_idx = []):
	# 初始化，主要把字典和列表pickle到文件，这样通过pickle文件进行交互
	with open(pickle_flie, 'w') as f1:
		pickle.dump((photo_url_dict, visited_idx), f1)
	print "init is OK! You can grab NOW"

def grab_url(base_url,pickle_flie):
	# 抓取网页，获取图片编号和图片地址的关系，存入字典，如果已经下载，则不放入字典
	with open(pickle_flie) as f2:
		photo_url_dict, visited_idx = pickle.load(f2)
		
	# page = requests.get(base_url, auth=HTTPBasicAuth(USER, PASSWORD)).text

	page = requests.get(base_url).text
	# doc = BeautifulSoup(page)
	
	doc = lxml.html.document_fromstring(page)
	for s in doc.xpath('//img/@data-original'):
	# for link in doc.find_all('img'):
	# 	s = link.get('data-original')
		photo_url = str(s).replace('cc//','cc/').replace('thumbs','wallpapers').replace('thumb','wallpaper')
		print photo_url
		idx = re.search(r'\d+',photo_url).group()
		if idx not in visited_idx:
			photo_url_dict[idx] = photo_url
			with open(pickle_flie, 'w') as f1:
				pickle.dump((photo_url_dict, visited_idx), f1)

def grab_photo(pickle_flie):
	# 传入一个photo的序号idx和一个图片的网址，然后进行下载并保存，文件名和idx一致
	with open(pickle_flie) as f3:
		photo_url_dict, visited_idx = pickle.load(f3)
	while photo_url_dict:
		photo_url =photo_url_dict.popitem()
		with open('%s.jpg' % photo_url[0], 'wb') as f:
			f.write(requests.get(photo_url[1]).content)
		print "photo %s has been downloaded!"		
		visited_idx.append(photo_url[0])
		with open(pickle_flie, 'w') as f1:
			pickle.dump((photo_url_dict, visited_idx), f1)
		time.sleep(10)
	print "dict's all photo OK!"

if __name__ == "__main__":
	# init(pickle_flie)
	# grab_url(base_url,pickle_flie)
	# grab_photo(pickle_flie)
	
	script = argv
	print "The script is called:", script
	print "1: init;/t2: grab url;/t3: grab photo; "
	print "Order must be 1>>>2>>>3"
	print "please tape your chioce!"

	chioce = raw_input('>')	

	if chioce == '1': init(pickle_flie)
	elif chioce == '2': grab_url(base_url,pickle_flie)
	elif chioce == '3': grab_photo(pickle_flie)
	else:print "chioce is empty!!!"




