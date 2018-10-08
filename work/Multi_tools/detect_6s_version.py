# -*- coding: utf-8 -*-
'''
@author: zyt
'''
import html_downloader
from bs4 import BeautifulSoup
import threading
import time
class timer(threading.Thread):  # The timer class is derived from the class threading.Thread
    def __init__(self, num, interval):
        threading.Thread.__init__(self)
        self.thread_num = num
        self.interval = interval
        self.thread_stop = False
    count =0
    def run(self):  # Overwrite run() method, put what you want the thread do here
        while not self.thread_stop:
            self.count = self.count +1
            html_cont =  html_downloader.HtmlDownloader().download("https://www.i4.cn/firmware_iPhone_iPhone%206s_iPhone8,1____80,120.html")
            soup = BeautifulSoup(html_cont, 'html.parser', from_encoding = 'utf-8')
            tr_list =soup.find(id='firmware_table').find_all('tr')
            Version =  tr_list[1].find_all('td')[3].get_text()
            
            if Version == '11.3.1':
                print (u'第'+str(self.count)+u'次刷新: 6s未刷新可刷机版本')
            else:
                print (u'6s已刷新!可刷机版本为：'+Version)
            time.sleep(self.interval)

    def stop(self):
        self.thread_stop = True
def get_information():
    thread1 = timer(1,60)
    thread1.start()
    time.sleep(86400)
    thread1.stop()
    return

if __name__ == '__main__':
    get_information()
