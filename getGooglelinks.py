import urllib
import mechanize
from bs4 import BeautifulSoup
import re
	
def getGoogleLinks(link,depth="10"):
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.addheaders=[('User-agent','chrome')]
	
	term = link.replace(' ','+')
	query = "http://www.google.com.hk/search?num=100&q="+term+"&start"+depth
	htmltext = br.open(query).read()
	soup = BeautifulSoup(htmltext)
	print "soup:",soup
	search = soup.findAll('div',attrs={'id':'search'})
	searchtext = str(search[0])
	print "searchtext:",searchtext
	soup1 = BeautifulSoup(searchtext)
	list_items = soup1.findAll('li')
	print "list_items:",list_items
	regex = "q(?!.*q).*?&amp"
	pattern = re.compile(regex)
	
	results_array = []
	
	for li in list_items:
		print li
		soup2 = BeautifulSoup(str(li))
		links = soup2.findAll('a')
		for item in links:
			print "links",item
		source_link = links[0]
		source_url = re.findall(pattern,str(source_link))
		if len(source_link)>0:
			results_array.append(str(source_url[0].replace("q=","").replace("&amp","")))
	return results_array
	
print getGoogleLinks("money","200")