# -*- coding:utf-8 -*-
import datetime
import sys
import time

from PIL import Image

import analyze
import search
import tools

reload(sys)
sys.setdefaultencoding('utf-8')
'''
主要思路：
1. 答题时使用adb截图，并将有用的部分截图
2. 通过有道ocr图片识别题目
3. 百度题目
4. 百度后结果与选项做匹配，匹配度最高的即为推荐答案

注： 部分题目由于识别或题目本身无法问题，可能搜索不到答案或推荐有误差，需自己根据题目情况进行抉择

'''


# 主函数
def main_start():

    # 获取屏幕尺寸
    size = tools.check_os()
    print u'当前使用手机的尺寸为：' + str(size)

    # 获取配置文件
    config = tools.get_config()
    is_auto = config['auto']
    is_yd_ocr = config['yd_ocr']
    # is_debug = config['debug']
    my_str = config['my_str']

    # 根据尺寸及配置文件，获取到当前问题区和空白区
    pixel_json = tools.get_pixel_config(size)
    blank_area = pixel_json['blank_area']
    # question_area = pixel_json['question_area']
    blank_area_point = blank_area['x1'], blank_area['y1'], blank_area['x2'], blank_area['y2']
    # question_area_point = question_area['x1'], question_area['y1'], question_area['x2'], question_area['y2']

    # 循环判断是否为答题页面
    question_num = 0
    crop_img_name = 'image/now.png'
    while True:
        while False:
            img = analyze.tell_and_get_image(is_auto, blank_area_point)
            if img is not None:
                question_num += 1
                break
            else:  # 若不是答题页
                if not is_auto:
                    print('没有发现题目页面')
                    exit(-1)
                print('没有发现答题页面，继续')
                time.sleep(0.8)  # 不是题目页面，休眠0.8秒后继续判断

        img = Image.open('image/backup.png')

        # 获取题目及选项
        start = datetime.datetime.now()  # 记录开始时间
        print u'开始时间为：'+str(start)
        tools.crop_image(img, crop_img_name)
        question, a1, a2, a3 = analyze.image_to_str(crop_img_name, is_yd_ocr, my_str)  # 图片转文字
        if question is None or question == '':
            print('\n没有识别题目')
            exit(-1)
        result_list = search.geturl(question, a1, a2, a3)  # 搜索结果
        for x in result_list:
            print x

        run_time = (datetime.datetime.now() - start).seconds
        print('本次运行时间为：{}秒'.format(run_time))
        if is_auto:
            time.sleep(25)  # 每一道题结束，休息10秒
        else:
            break


if __name__ == '__main__':
    main_start()
