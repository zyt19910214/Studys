# -*- coding:utf-8 -*-
import tools
import os
from PIL import Image
import md5
import urllib
import urllib2
import random
import json
import base64
import re

appKey = '23d3a81ae3eee2ab'
secretKey = 'ExTaNpz88GgDjPrWASfWng7CivcZueJe'
httpClient = None


# 分辨是否为答题页面,若是则返回图片对象
def tell_and_get_image(is_auto, black_point):
    tools.pull_from_screen()  # 截图
    backup_img = None
    if os.path.exists('image/backup.png'):
        backup_img = Image.open('image/backup.png')
    else:
        print('image/backup.png位置图片不存在')
        exit(-1)
    start_x, start_y, end_x, end_y = black_point
    if not is_auto:
        return backup_img
    is_answer_page = False
    is_end = False
    for w in range(start_x, end_x, 100):  # 根据颜色判断是否是题目页面
        for h in range(start_y, end_y, 10):
            pixel = backup_img.getpixel((w, h))  # 获取像素点
            r, y, b = pixel[0], pixel[1], pixel[2]
            is_answer_page = r == 0xff and y == 0xff and b == 0xff
            if not is_answer_page:
                is_end = True
                break
        if is_end:
            break
    if is_answer_page:
        return backup_img
    else:
        backup_img.close()
        return None


def image_to_str(image_obj, is_yd_orc, my_str):
    try:
        f = open(image_obj, 'rb')  # 二进制方式打开图文件
        img = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
        f.close()
        detectType = '10011'
        imageType = '1'
        langType = 'zh-en'
        salt = random.randint(1, 65536)

        sign = appKey + img + str(salt) + secretKey
        m1 = md5.new()
        m1.update(sign)
        sign = m1.hexdigest()
        data = {'appKey': appKey, 'img': img, 'detectType': detectType, 'imageType': imageType,
                'langType': langType,
                'salt': str(salt), 'sign': sign, 'docType': 'json'}
        data = urllib.urlencode(data)
        req = urllib2.Request('http://openapi.youdao.com/ocrapi', data)

        # response是HTTPResponse对象
        response = urllib2.urlopen(req)
        decode_json = json.loads(response.read())

        my_list = decode_json['Result']['regions']
        all_list = []
        # print  my_list
        for n in my_list:
            # print len(n['lines'])
            for t in n['lines']:
                for x in t['words']:
                    all_list.append(x['text'])
                all_list.append('-')
        my_str = "".join(all_list)
        print my_str
        question = my_str.split('?')[0]

        if '-' in question:
            re.sub('-', '', question)
        else:
            pass
        print question+'?'
        answser1 = my_str.split('-')[-2]
        answser2 = my_str.split('-')[-3]
        answser3 = my_str.split('-')[-4]
        # print answser1
        # print answser2
        # print answser3
        # print answser4
        return question+'?', answser1, answser2, answser3
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()
