
# Create your tests here.

#coding=utf-8
import urllib
import re
import sqlite3

# conn = sqlite3.connect('db.sqlite3')
# c = conn.cursor()
# c.execute('select name from account_person order by sort')
# print(c.fetchone())
#
# def getHtml(url):
#     page = urllib.urlopen(url)
#     html = page.read()
#     return html
#
# def getImg(html):
#     reg = r'src="(.+?\.jpg)"'
#     regtxt = r'title="" href'
#     imgre = re.compile(reg)
#     imglist = re.findall(imgre,html)
#     txtre = re.compile(regtxt)
#     txtlist = re.findall(txtre,html)
#     x = 0
#     y = 0;
#     for imgurl in imglist:
#         urllib.urlretrieve(imgurl,'%s.jpg' % x)
#         x+=1
#
#
# html = getHtml("http://beijing.anjuke.com/sale/p2/#filtersort")
#
# print getImg(html)
#
# import urllib2
# class house:
#     def __init__(self,baseUrl,seeLZ):
#         self.baseUrl = baseUrl
#         self.eeLZ = '?see_lz='

def test(request):
    print request.POST.get('')
    return