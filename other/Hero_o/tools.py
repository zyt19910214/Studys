# coding=utf-8
import subprocess
import os
import json
from PIL import Image
import base64
import yd_orc

shot_way = 3


# 获取分辨率配置文件
def get_pixel_config(size):
    width, height = size
    config_path = 'config/{}x{}.json'.format(width, height)
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return json.load(f)
    else:  # 加载
        print('请配置对应分辨率')
        exit(-1)


# 获取配置文件
def get_config():
    config_file = 'config.json'
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            return json.load(f)
    else:
        print('请检查根目录下是否存在配置文件 config.json')
        exit(-1)


# 检查adb是否安装,获取屏幕大小
def check_os():
    size_str = os.popen('adb shell wm size').read()
    if not size_str:
        print('请安装ADB,并打开调试模式')
        exit(-1)
    else:
        size_x_y = size_str.split(':')[1].strip()
        x, y = size_x_y.split('x')
        size = x, y
        return size


# 屏幕截图，参考 跳一跳截图方法 https://github.com/wangshub/wechat_jump_game/blob/master/common/screenshot.py
def pull_from_screen():
    global shot_way
    if shot_way < 0:
        print('暂不支持当前设备')
        exit(-1)
    shot_screen()
    try:
        Image.open('image/backup.png').load()
    except Exception:  # 递归调用，直到找到截图方式
        shot_way -= 1
        pull_from_screen()


# 截取图片
def crop_image(image, image_name):
    w = image.size[0]
    h = image.size[1]
    region = image.crop((0, 300, w, h-700))  # 裁剪的区域
    region.save(image_name)
    f = open(image_name, 'rb')  # 二进制方式打开图文件
    base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
    f.close()


# 具体截图方法，按优先级排序
def shot_screen():
    global shot_way
    if 1 <= shot_way <= 3:
        process = subprocess.Popen(
            'adb shell screencap -p',
            shell=True, stdout=subprocess.PIPE)
        binary_img = process.stdout.read()
        if shot_way == 2:
            binary_img = binary_img.replace(b'\r\n', b'\n')
        elif shot_way == 1:
            binary_img = binary_img.replace(b'\r\r\n', b'\n')
        f = open('image/backup.png', 'wb')
        f.write(binary_img)
        f.close()
    elif shot_way == 0:
        os.system('adb shell screencap -p /sdcard/answer_backup.png')


