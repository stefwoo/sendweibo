#################################
#author:seaven
#webpage:www.skyey.com.cn
#e-mail:seavens@qq.com
#################################
import urllib2,threading,re,datetime,sys
from urlparse import urlsplit
from bs4 import *
from filehelper import *
from stringutil import *
from mail import *

def compare_data(title,date,price):
        #print os.path.isfile('carsurl.txt') #如果不存在就返回False
        refDate = re.findall(r'\d{1,2}[-|\\/]\d{1,2}',str(date[0])) #发布日期
        p = float(re.findall(r'\d+\.?\d*', str(price[0]))[0]) #价格
        print strip_tags(str(title[0])),'--',p,'万'
        mailtext=''
        if p<=5 and len(refDate)==0: ##如果价格小于5万，并且发布日期是今天 。这里可以根据需要修改
                pat = re.compile(r'href="([^"]*)"')
                pat2 = re.compile(r'http')
                for item in title:
                         h = pat.search(str(item))
                         href = h.group(1)
                         if pat2.search(href):
                             ans = href
                         else:
                             ans = url+href

                         now = datetime.datetime.now()#now.strftime('%Y-%m-%d %H:%M:%S')
                         temp = strip_tags(str(title[0]))+'--'+ans+' --'+str(p)+'万'+'---'+now.strftime('%Y-%m-%d %H:%M')+';\r\n'
                         readContent = read_content('carsurl.txt')#读取已经保存的URL
                         if readContent.find(ans)<0: #如果url不存在就写入文本，并且发送email
                                 mailtext=temp
                                 write_file('carsurl.txt',temp)

        return mailtext
          
def down_task(url):
        req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
        webpage = urllib2.urlopen(req)
        soup = BeautifulSoup(webpage.read(),fromEncoding="GB18030")
        print '正在运行...',get_now_time()
        #download the book chaptert
        mailtext=[]
        for item in soup.findAll('tr'):
                title = item.find_all('a',{'class':'t'})
                date = item.find_all('span',{'class':'c_999'})
                price = item.find_all('b',{'class':'pri'})
                if len(price)>0 and len(date)>0:
                        temptext = compare_data(title,date,price)
                        if len(temptext)>0:#返回如果有数据就添加到mailtext
                                mailtext.append(temptext)
        if len(mailtext)>0:
                send_mail('seavens@qq.com',['seavens@qq.com'],'二手车参考信息',''.join(mailtext))
                
#download these tow books
#down_task('http://cd.58.com/jingjijiaoche/pn2/')
def main_fn():
        down_task('http://cd.58.com/jingjijiaoche/pn2/')
        global t        #Notice: use global variable!
        t = threading.Timer(5.0, main_fn) #5秒获取一次，可以改成需要的时间，比如：60.0*10（10分钟获取一次）
        t.start()

t = threading.Timer(5.0, main_fn) #5秒获取一次，可以改成需要的时间，比如：60.0*10（10分钟获取一次）
t.start()