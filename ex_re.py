#! /usr/bin/python
# coding=utf-8
import re
from urlparse import urlparse
s = "http://wallpapers.wallbase.cc/rozne/wallpaper-3032674.jpg"

# print re.search('\d+', s).group()

o = urlparse(s)
print o
