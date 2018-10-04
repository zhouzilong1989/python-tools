#coding:utf-8
import urllib
import re

def get_html(url):
    page = urllib.urlopen(url)#打开网页
    htmlcode = page.read()#读取页面源码
    return htmlcode

def get_image(url, htmlcode):
    reg = r'src="(.*?\.jpg)" '  # 正则表达式
    reg_img = re.compile(reg)  # 编译一下，运行更快
    imglist = reg_img.findall(htmlcode)  # 进行匹配
    x = 0
    if url.startswith("https://"):
        url2 = url[8:url.__len__()-1]
    elif url.startswith("http://"):
        url2 = url[7:url.__len__()-1]
        url2 = url[:url.__len__()-1]
    else:
    print url2
    for img in imglist:
        print x
        print img
        urllib.urlretrieve(img, 'Image/%(1)s_%(2)d.jpg' % {'1':url2, '2':x})
        x += 1

print u'请输入url:'
url = raw_input().strip()
print url
if url:
    pass
else:
    url = 'http://tieba.baidu.com/p/1753935195'
html_code = get_html(url)
get_image(url, html_code)

