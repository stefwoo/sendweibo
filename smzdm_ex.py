#! /usr/bin/env python
#coding=utf-8
from lxml import etree, html
import urllib2
import re

smzdm_amazon = u'http://fx.smzdm.com/?mall=%E4%BA%9A%E9%A9%AC%E9%80%8A%E4%B8%AD%E5%9B%BD'
req = 'http://fx.smzdm.com/go/142615'

def amazon(req):
    msg = urllib2.urlopen(req).read()
    p=re.compile(r"href = '(.*)'")#</?[^>]+>
    url = p.findall(msg)[0]
    print url
    return re.sub('joyo01f-23','joyo02f-23',url)

print type(amazon(req))

#root = html.document_fromstring(msg)
#print etree.tostring(root, pretty_print=True)
#print root.xpath("//script/")[0]

#def expand(format, d, marker = "", safe = False):
#    if safe:
#        def lookup(w): return d.get(w, w.jion(marker*2))
#    else:
#        def lookup(w): return d(w)
#    parts = format.split(marker)
#    parts[1::2] = map(lookup, parts[1::2]
#    return ''.join(parts)
#
#if __name__ = '__main__':
#    print expand('just "a" test',('a' = 'one'))
