#! /usr/bin/python
# coding=utf-8

import requests
from requests.auth import HTTPBasicAuth
USER = "stefwoo"
PASSWORD = "Br1sjhhrhl"
m = requests.get('http://wallbase.cc', auth=HTTPBasicAuth(USER, PASSWORD))
r = requests.get('http://wallbase.cc/search?purity=001')
print r.status_code
print r.text.encode('utf-8')

# run()
# grab_photo(idx,photo_url)

# idx = "246088"
# photo_url = "http://wallpapers.wallbase.cc/high-resolution/wallpaper-246088.jpg"
# http://wallpapers.wallbase.cc/high-resolution/wallpaper-229987.jpg
# http://wallbase.cc/wallpaper/229987
# http://wallpapers.wallbase.cc/high-resolution/wallpaper-229987.jpg
# http://wallbase.cc/wallpaper/246088
# http://wallpapers.wallbase.cc/high-resolution/wallpaper-246088.jpg
# http://wallbase.cc/search?q==(pussy)&color=&section=wallpapers&q==(pussy)&res_opt=eqeq&res=0x0&order_mode=desc&thpp=32&purity=001&board=213&aspect=0.00
# http://wallbase.cc/search?q==(brunettes)&purity=001
# http://wallbase.cc/search?purity=100

# //*[@id="thumb3033056"]
# import requests
# import lxml.html
# page = requests.get('http://tieba.baidu.com/p/2166231880').text
# doc = lxml.html.document_fromstring(page)
# for idx, el in enumerate(doc.cssselect('img.BDE_Image')):
#     with open('%03d.jpg' % idx, 'wb') as f:
#         f.write(requests.get(el.attrib['src']).content)

# <img src="http://static.wallbase.cc/front/6/images/transparent.gif" data-original="http://thumbs.wallbase.cc//rozne/thumb-3032934.jpg" class="file lazy lazyGO">
# from bs4 import BeautifulSoup
# page = requests.get('http://wallbase.cc/search?purity=100').text
# soup = BeautifulSoup(page)
# for link in soup.find_all('img'):
# 	s = link.get('data-original')
# 	# print type(s)
# 	# print str(s).replace('thumbs','wallpapers')
# 	s1 = str(s).replace('cc//','cc/').replace('thumbs','wallpapers').replace('thumb','wallpaper')
# 	print s1
# 	# print link

# >>> import cPickle as pickle
# >>> t1 = ('this is a string', 42, [1, 2, 3], None)
# >>> t1
# ('this is a string', 42, [1, 2, 3], None)
# >>> p1 = pickle.dumps(t1)
# >>> p1
# "(S'this is a string'/nI42/n(lp1/nI1/naI2/naI3/naNtp2/n."
# >>> print p1
# (S'this is a string'
# I42
# (lp1
# I1
# aI2
# aI3
# aNtp2
# .
# >>> t2 = pickle.loads(p1)
# >>> t2
# ('this is a string', 42, [1, 2, 3], None)
# >>> p2 = pickle.dumps(t1, True)
# >>> p2
# '(U/x10this is a stringK*]q/x01(K/x01K/x02K/x03eNtq/x02.'
# >>> t3 = pickle.loads(p2)
# >>> t3
# ('this is a string', 42, [1, 2, 3], None)