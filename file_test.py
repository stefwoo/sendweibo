#! /usr/bin/python
# coding=utf-8
import os

user_FILE = 'user.msg'
# def load_userlist(filename=user_FILE):
filename=user_FILE
user_list = []
# try:
filepath = os.path.join(os.path.dirname(__file__), filename)
f = open(filepath,'a')
some = {'lady gaga':'lady@kiss.com','jordan':'jordan@kiss.com'}
print type(some)
# print ','.join(i for i in some)
# for i in some:
# 	f.write(i)
# 	f.write(',')
# f.write(','.join(i for i in some))
# m = f.readlines()#.strip()
# m.append(some)
# print ','.join(i for i in m)
f.close()

for i in some:print i

print str(some)

s=str(some)

for i in s.split(','):print i

string = "lady gaga:lady@kiss.com,jordan:jordan@kiss.com"
dict1 = {}
for i in string.split(','):
	print i
	x = i.split(':')
	dict1[x[0]]=x[1]
print dict1

d = eval(s)
print type(d)
print d


s1="{'lady gaga':'lady@kiss.com','jordan':'jordan@kiss.com'}"
print eval(s1)
print s1
import json
# print '1'
# dictinfo = json.loads(s1) 
# json.loads("{'k':1,'v':2}")
print json.loads('"\\"fo\\bar"')
print json.loads('{"jordan": "jordan@163.com", "lady gaga":"ladygaga@163.com"}')

print json.loads(json.dumps(s1))
dx = json.loads(json.dumps(d))
print type(dx) 
# print lambda i:for m in some
# print lambda i: x for x in i(some)

# print m
# print type(m)
# # if m:
# # 	acc_tk_list.append(m)
# # 	print "===> Get the access_token from file token-record.log : ", acc_tk_list[0]
# # else:
# # 	print "===> roken-record.log is None!"
# print [i for i in m]
# f.close()
# 	# except IOError:
# 	# 	print "===> File token-record.log does not exist."
# 	# Pass
# 	# acc_tk_list
# usr = 'stefwoo,wffice'
# l=usr.split(',')
# print l
# print type(l)
# for i in l:
# 	print i
# print i:i for i in l
# x = [i for i in l]
# print x