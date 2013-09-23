import urllib2
import socket

class MyException(Exception):
    pass

try:
	print "first"
	urllib2.urlopen("http://twitter.com", timeout = 1)
# help(urllib2)
# urllib2.urlopen("http://www.baidu.com",timeout = 1)
# urllib2.urlopen()
except urllib2.URLError, e:
    # print e
    print "second"
    if isinstance(e.reason, socket.timeout):
        raise MyException("There was an error: %r" % e)
    else:
        # reraise the original error
        raise
# print "hello world"