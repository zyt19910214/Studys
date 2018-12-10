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



count1 = 0

now_url = 'https://m.mzitu.com/all/'
r = requests.get(now_url,headers=Hostreferer)
soup = BeautifulSoup(r.text,'lxml')
now = datetime.datetime.now()
yes = now+datetime.timedelta(days=-1)
time_str = yes.strftime('%m-%d')

url_list = soup.find_all('a',class_='clear')
url_list2 = [url for url in url_list if time_str in url.text]
if url_list2:
    path = os.getcwd()+'/url/'
    for i in os.listdir(path):
        path_file = os.path.join(path, i)
        if os.path.isfile(path_file):
            print(path_file)
            os.remove(path_file)
    for url in url_list2:
        count1 += 1
        title = url.text
        if os.path.exists('./url/'+str(count1)+'.txt'):
            os.remove('./url/'+str(count1)+'.txt')
        fs = open('./url/'+str(count1)+'.txt', 'a')
        fs.write(title.encode('utf8')+'\n')

        # path = 'D:\\pics\\' + title
        # if os.path.exists(path):
        #     pass
        # else:
        #     os.mkdir(path)
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

                    fs.write(img_url+',')
else:
    pass
print (now_url+' is crawed')
