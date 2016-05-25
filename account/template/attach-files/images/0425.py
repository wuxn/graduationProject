#! /usr/bin/env python
#coding=utf-8
import re,datetime,time
from bs4 import BeautifulSoup
import urllib2,urllib



class ReadAJK(object):
    
    def __init__(self):
        self.html = ''
        self.url_list = [
            'http://beijing.anjuke.com/sale/o5/',
            # 'http://beijing.anjuke.com/sale/p2/#filtersort'
        ]
        self.img_path = '/Users/xiaonawu/Documents/working/Python/register/account/template/attach-files/images' #要保存到哪，图片绝对路径
        self.img_list = []
        self.obj = []
        self.txt = []
    
    def read_url(self):
        for url in self.url_list:
            
            temp = {'img_name':'','desc':''}
            self.html = urllib2.urlopen(url)
            if not self.html:
                continue
            soup = BeautifulSoup(self.html)
            print soup.find_all("div",class_="house-title")[0]
            s = soup.find_all('li',class_='fst-li')
            if not s:
                continue
            img = s[0].find_all('img')[0]['src']
            temp['img_name'] = img.split('/'[-1])
            self.img_list.append(img)

            for title in soup.select('.house-title a'):
                print title.get_text()+"/"


            # <p name="dromouse"><b>The Dormouse's story</b></p>

            
            
    def down_img(self):
        for url in self.img_list:
            u_img = urllib2.urlopen(url)
            f = open(self.img_path+url.split('/')[-1],'w')
            f.write(u_img.read())
            f.close()
        self.img_list = []

    
    
    
read = ReadAJK()
read.read_url()
        