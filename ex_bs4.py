#! /usr/bin/python
# coding=utf-8
import requests,re
from bs4 import BeautifulSoup
base_url = u'http://wallbase.cc/search?purity=100'
page = requests.get(base_url).text
print page.encode('utf-8')
soup = BeautifulSoup(page)
for link in soup.find_all('img'):
	s = link.get('data-original')
	photo_url = str(s).replace('cc//','cc/').replace('thumbs','wallpapers').replace('thumb','wallpaper')
	print photo_url
	idx = re.search(r'\d+',photo_url).group()
	print idx