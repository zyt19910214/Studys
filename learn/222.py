# -*- coding: utf-8 -*-
# @File  : 111.py
# @Author: zyt
# @Date  : 2018/10/8 10:27
# @Desc  :

import requests
from bs4 import BeautifulSoup
import os
import datetime

Hostreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer':'http://www.mzitu.com'
               }
Picreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer':'http://i.meizitu.net'
}
for xx in range(0,1):
    now_url = 'https://m.mzitu.com/all/'
    r = requests.get(now_url,headers=Hostreferer)
    soup = BeautifulSoup(r.text,'lxml')
    now = datetime.datetime.now()
    yes = now+datetime.timedelta(days=-1)
    time_str = yes.strftime('%m-%d')
    print(time_str)
    url_list = soup.find_all('a',class_='clear')
    print(url_list)
    for url in url_list:
        if time_str in url.text:
            print(url)
        else:
            pass


    for url in url_list:
        x = url.find_all('img',class_='featured-image aligncenter lazy')
        if x:
            path = 'D:\\pics\\'+url.get('title')
            if os.path.exists(path):
                pass
            else:
                os.mkdir(path)
            s_url = url.get('href')
            new_r = requests.get(s_url,headers=Hostreferer)
            soup2 = BeautifulSoup(new_r.text,'lxml')
            count = soup2.find('span',class_='prev-next-page').text.split('/')[1][:-1]

            for i in range(1,int(count)+1):
                next_img = requests.get(s_url+'/'+str(i),headers=Hostreferer)
                soup2 = BeautifulSoup(next_img.text, 'lxml')
                img_l = soup2.find('figure')
                if img_l is not None:
                    xxx = img_l.find('img')
                    if xxx is not None:
                        img_url = xxx.get('src')
                        if os.path.exists(path + '\\' + img_url.split('/')[-1]):
                            pass
                        else:
                           print ('ok')
                           # img_r = requests.get(img_url, headers=Picreferer)
                           # try:
                           #     f = open(path + '\\' + img_url.split('/')[-1], 'wb')
                           #     f.write(img_r.content)
                           #     f.close()
                           # except Exception as e:
                           #     print (e)
            print (path.split('\\')[-1] + ' is crawed')
    print (now_url+' is crawed')