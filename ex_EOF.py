import requests,time,sys
# while True:
# 	try:
# 		print requests.get("https://github.com").status_code
# 		time.sleep(10)
# 	except:
# 		print "Unexpected error:", sys.exc_info()
# 		# pass

# 	try:
# 		print requests.get("https://github.com",verify=False).status_code
# 		time.sleep(10)
# 	except:
# 		print "Unexpected error:", sys.exc_info()
# 		# pass

r = requests.get('http://wallbase.cc/search?purity=100')
print r.text.encode('')