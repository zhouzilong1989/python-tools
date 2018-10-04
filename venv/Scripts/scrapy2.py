#coding=utf-8
import urllib
import urllib2
import re
agent = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0"
headers = {"user-Agent":agent}
url="http://news.sina.com.cn/"
req = urllib2.Request(url = url,headers = headers)
#res = urllib2.urlopen(req)
data = urllib2.urlopen(req).read()
data2 = data.decode("utf-8","ignore")
pat = 'href="(http://news.sina.com.cn/.*?)"'
allurl = re.compile(pat).findall(data2)
for i in range(0, len(allurl)):
    try:
        print("第"+str(i))
        thisurl=allurl[i]
        print thisurl
        file="D:/MyFile/" + str(i) + ".html"
        urllib.urlretrieve(thisurl, file)
    except urllib.error.URLErroe as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)