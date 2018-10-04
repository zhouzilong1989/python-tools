#coding:utf-8
import requests
import json

key = '******' #input your tuling robot key
while True:
    print u'我:'
    info = raw_input().strip()
    url = 'http://www.tuling123.com/openapi/api?key=' + key + '&info=' + info
    res = requests.get(url)
    print res.text
    res.encoding = 'utf-8'
    jd = json.loads(res.text)
    print 'Tuling: ' + jd['text']
