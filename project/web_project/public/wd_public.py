# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from PIL import Image
from functools import reduce
import math
import operator
import time
import os
import inspect
import allure
import win32gui
import win32api
import win32con
import yaml


class WDPublic(object):
    """封装公共API"""

    def __init__(self, name):
        """
        路径是要运行的app安装路径+运行程序

        远程启动参数browser browserName=chrome,chrome_binary="C:\Program Files (x86)\PoliceVP\PoliceVP.exe"
        """
        if "remote" in name:
            http = name.split("=>")[1]
            self.driver = webdriver.Remote(command_executor=http, desired_capabilities=DesiredCapabilities.CHROME)
        elif "path" in name:
            path = name.split("=>")[1]
            _browser_url = path
            chrome_options = Options()
            chrome_options.binary_location = _browser_url
            self.driver = webdriver.Chrome(chrome_options=chrome_options)
        elif name == "firefox":
            self.driver = webdriver.Firefox()
        elif name == "chrome":
            self.driver = webdriver.Chrome()
        elif name == "internet explorer" or name == "ie":
            self.driver = webdriver.Ie()
        elif name == "opera":
            self.driver = webdriver.Opera()
        elif name == 'edge':
            self.driver = webdriver.Edge()

    def element_wait(self, xpath, secs=30):
        """
        等待元素存在，默认等待30秒，每1秒扫描一次
        """
        if "=>" not in xpath:
            by = "xpath"
            value = xpath
        else:
            by = xpath.split("=>")[0]
            value = xpath.split("=>")[1]
            if by == "" or value == "":
                raise NameError(
                    "Grammatical errors,reference: 'id=>username'.")
        if by == "id":
            return WebDriverWait(self.driver, secs, 1).until(ec.presence_of_element_located((By.ID, value)))
        elif by == "name":
            return WebDriverWait(self.driver, secs, 1).until(ec.presence_of_element_located((By.NAME, value)))
        elif by == "class":
            return WebDriverWait(self.driver, secs, 1).until(ec.presence_of_element_located((By.CLASS_NAME, value)))
        elif by == "link_text":
            return WebDriverWait(self.driver, secs, 1).until(ec.presence_of_element_located((By.LINK_TEXT, value)))
        elif by == "xpath":
            return WebDriverWait(self.driver, secs, 1).until(ec.presence_of_element_located((By.XPATH, value)))
        elif by == "css":
            return WebDriverWait(self.driver, secs, 1).until(ec.presence_of_element_located((By.CSS_SELECTOR, value)))
        else:
            raise NoSuchElementException(
                "Not find element, Please check the syntax error.")

    def element_wait_not_presence(self, xpath, secs=30):
        """
        等待元素不存在，默认等待30秒，每1秒扫描一次
        """
        if "=>" not in xpath:
            by = "xpath"
            value = xpath
        else:
            by = xpath.split("=>")[0]
            value = xpath.split("=>")[1]
            if by == "" or value == "":
                raise NameError(
                    "Grammatical errors,reference: 'id=>username'.")
        if by == "id":
            return WebDriverWait(self.driver, secs, 1).until_not(ec.presence_of_element_located((By.ID, value)))
        elif by == "name":
            return WebDriverWait(self.driver, secs, 1).until_not(ec.presence_of_element_located((By.NAME, value)))
        elif by == "class":
            return WebDriverWait(self.driver, secs, 1).until_not(ec.presence_of_element_located((By.CLASS_NAME, value)))
        elif by == "link_text":
            return WebDriverWait(self.driver, secs, 1).until_not(ec.presence_of_element_located((By.LINK_TEXT, value)))
        elif by == "xpath":
            return WebDriverWait(self.driver, secs, 1).until_not(ec.presence_of_element_located((By.XPATH, value)))
        elif by == "css":
            return WebDriverWait(self.driver, secs, 1).until_not(ec.presence_of_element_located((By.CSS_SELECTOR, value)
                                                                                                ))
        else:
            raise NoSuchElementException(
                "Not find element, Please check the syntax error.")

    def element_wait_visible(self, xpath, secs=30):
        """
        等待元素可见，默认等待30秒，每1秒扫描一次
        """
        if "=>" not in xpath:
            by = "xpath"
            value = xpath
        else:
            by = xpath.split("=>")[0]
            value = xpath.split("=>")[1]
            if by == "" or value == "":
                raise NameError(
                    "Grammatical errors,reference: 'id=>username'.")
        if by == "id":
            return WebDriverWait(self.driver, secs, 1).until(ec.visibility_of_element_located((By.ID, value)))
        elif by == "name":
            return WebDriverWait(self.driver, secs, 1).until(ec.visibility_of_element_located((By.NAME, value)))
        elif by == "class":
            return WebDriverWait(self.driver, secs, 1).until(ec.visibility_of_element_located((By.CLASS_NAME, value)))
        elif by == "link_text":
            return WebDriverWait(self.driver, secs, 1).until(ec.visibility_of_element_located((By.LINK_TEXT, value)))
        elif by == "xpath":
            return WebDriverWait(self.driver, secs, 1).until(ec.visibility_of_element_located((By.XPATH, value)))
        elif by == "css":
            return WebDriverWait(self.driver, secs, 1).until(ec.visibility_of_element_located((By.CSS_SELECTOR, value)))
        else:
            raise NoSuchElementException(
                "Not find element, Please check the syntax error.")

    def element_wait_not_visible(self, xpath, secs=30):
        """
        等待元素不可见，默认等待30秒，每1秒扫描一次
        """
        if "=>" not in xpath:
            by = "xpath"
            value = xpath
        else:
            by = xpath.split("=>")[0]
            value = xpath.split("=>")[1]
            if by == "" or value == "":
                raise NameError(
                    "Grammatical errors,reference: 'id=>username'.")
        if by == "id":
            return WebDriverWait(self.driver, secs, 1).until_not(ec.visibility_of_element_located((By.ID, value)))
        elif by == "name":
            return WebDriverWait(self.driver, secs, 1).until_not(ec.visibility_of_element_located((By.NAME, value)))
        elif by == "class":
            return WebDriverWait(self.driver, secs, 1).until_not(ec.visibility_of_element_located((By.CLASS_NAME, value)
                                                                                                  ))
        elif by == "link_text":
            return WebDriverWait(self.driver, secs, 1).until_not(ec.visibility_of_element_located((By.LINK_TEXT, value))
                                                                 )
        elif by == "xpath":
            return WebDriverWait(self.driver, secs, 1).until_not(ec.visibility_of_element_located((By.XPATH, value)))
        elif by == "css":
            return WebDriverWait(self.driver, secs, 1).until_not(ec.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                                   value)))
        else:
            raise NoSuchElementException(
                "Not find element, Please check the syntax error.")

    def toast_msg_text(self, xpath, msg, secs=15):
        """
        单独对toast进行判断，默认15秒每秒扫描一次，查询toast的提示信息是否正确，并返回验证结果
        """
        if "=>" not in xpath:
            by = "xpath"
            value = xpath
        else:
            by = xpath.split("=>")[0]
            value = xpath.split("=>")[1]
            if by == "" or value == "":
                raise NameError(
                    "Grammatical errors,reference: 'id=>username'.")
        if by == "id":
            return WebDriverWait(self.driver, secs, 1).until(ec.text_to_be_present_in_element((By.ID, value), msg))
        elif by == "name":
            return WebDriverWait(self.driver, secs, 1).until(ec.text_to_be_present_in_element((By.NAME, value), msg))
        elif by == "class":
            return WebDriverWait(self.driver, secs, 1).until(ec.text_to_be_present_in_element((By.CLASS_NAME, value),
                                                                                              msg))
        elif by == "link_text":
            return WebDriverWait(self.driver, secs, 1).until(ec.text_to_be_present_in_element((By.LINK_TEXT, value),
                                                                                              msg))
        elif by == "xpath":
            return WebDriverWait(self.driver, secs, 1).until(ec.text_to_be_present_in_element((By.XPATH, value), msg))
        elif by == "css":
            return WebDriverWait(self.driver, secs, 1).until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, value),
                                                                                              msg))
        else:
            raise NoSuchElementException(
                "Not find element, Please check the syntax error.")

    def get_element(self, xpath):
        """
        封装获取对象，默认使用xpath
        id=>name
        """
        element = self.element_wait(xpath)
        return element

    def get_sub_element(self, parent_element, xpath):
        """
        封装获取对象，默认使用xpath
        id=>name
        """
        if "=>" not in xpath:
            by = "xpath"
            value = xpath
        else:
            by = xpath.split("=>")[0]
            value = xpath.split("=>")[1]
        if str(type(parent_element)) != "<class 'selenium.webdriver.remote.webelement.WebElement'>":
            parent_element = self.get_element(parent_element)

        if by == "id":
            element = parent_element.find_element_by_id(value)
        elif by == "name":
            element = parent_element.find_element_by_name(value)
        elif by == "class":
            element = parent_element.find_element_by_class_name(value)
        elif by == "link_text":
            element = parent_element.find_element_by_link_text(value)
        elif by == "xpath":
            element = parent_element.find_element_by_xpath(value)
        elif by == "css":
            element = parent_element.find_element_by_css_selector(value)
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        return element

    def get_elements(self, xpath):
        """
        封装获取一组对象，默认使用xpath
        id=>name
        """
        if "=>" not in xpath:
            by = "xpath"
            value = xpath
        else:
            by = xpath.split("=>")[0]
            value = xpath.split("=>")[1]
            if by == "" or value == "":
                raise NameError(
                    "Grammatical errors,reference: 'id=>username'.")

        if by == "id":
            elements = self.driver.find_elements_by_id(value)
        elif by == "name":
            elements = self.driver.find_elements_by_name(value)
        elif by == "class":
            elements = self.driver.find_elements_by_class_name(value)
        elif by == "link_text":
            elements = self.driver.find_elements_by_link_text(value)
        elif by == "xpath":
            elements = self.driver.find_elements_by_xpath(value)
        elif by == "css":
            elements = self.driver.find_elements_by_css_selector(value)
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        return elements

    def input(self, xpath, text):
        """
        封装输入方法
        :param xpath: 定位信息，xpath or webElement
        :param text: 输入文本
        """
        if str(type(xpath)) != "<class 'selenium.webdriver.remote.webelement.WebElement'>":
            xpath = self.get_element(xpath)
        xpath.send_keys(text)

    def clear(self, xpath):
        """
        封装清空文本框方法
        :param xpath: 定位信息，xpath or webElement
        """
        if str(type(xpath)) != "<class 'selenium.webdriver.remote.webelement.WebElement'>":
            xpath = self.get_element(xpath)
        xpath.clear()

    def click(self, xpath):
        """
        封装点击方法
        :param xpath: 定位信息，xpath or webElement
        """
        if str(type(xpath)) != "<class 'selenium.webdriver.remote.webelement.WebElement'>":
            xpath = self.get_element(xpath)
        xpath.click()

    def right_click(self, xpath):
        """
        封装右键操作
        :param xpath: 定位信息，xpath or webElement
        """
        if str(type(xpath)) != "<class 'selenium.webdriver.remote.webelement.WebElement'>":
            xpath = self.get_element(xpath)
        ActionChains(self.driver).context_click(xpath).perform()

    def move_to_element(self, xpath):
        """
        封装移动元素方法
        :param xpath: 定位信息，xpath or webElement
        """
        if str(type(xpath)) != "<class 'selenium.webdriver.remote.webelement.WebElement'>":
            xpath = self.get_element(xpath)
        ActionChains(self.driver).move_to_element(xpath).perform()

    def move_to_element_with_offset(self, xpath, x, y):
        """
        封装移动元素到指定坐标并点击方法
        :param xpath: 定位信息，xpath or webElement
        :param x: 指定x坐标
        :param y: 指定y坐标
        """
        if str(type(xpath)) != "<class 'selenium.webdriver.remote.webelement.WebElement'>":
            xpath = self.get_element(xpath)
        ActionChains(self.driver).move_to_element_with_offset(xpath, x, y).click().perform()

    def double_click(self, xpath):
        """
        封装双击方法
        :param xpath: 定位信息，xpath or webElement
        """
        if str(type(xpath)) != "<class 'selenium.webdriver.remote.webelement.WebElement'>":
            xpath = self.get_element(xpath)
        ActionChains(self.driver).double_click(xpath).perform()

    def drag_and_drop(self, el_xpath, ta_xpath):
        """
        封装拖拽方法
        :param el_xpath: 原元素对象定位信息，xpath or webElement
        :param ta_xpath: 目标元素对象定位信息，xpath or webElement
        """
        if str(type(el_xpath)) != "<class 'selenium.webdriver.remote.webelement.WebElement'>":
            el_xpath = self.get_element(el_xpath)
        if str(type(ta_xpath)) != "<class 'selenium.webdriver.remote.webelement.WebElement'>":
            ta_xpath = self.get_element(ta_xpath)
        ActionChains(self.driver).drag_and_drop(el_xpath, ta_xpath).perform()

    def click_text(self, link):
        """
        封装点击link方法
        :param link: 目录link
        """
        self.driver.find_element_by_partial_link_text(link).click()

    def quit(self):
        """
        封装退出所有窗口的方法
        """
        self.driver.quit()

    def close(self):
        """
        封装关闭当前窗口的方法
        """
        self.driver.close()

    def submit(self, xpath):
        """
        封装提交from的方法
        :param xpath: 定位信息，xpath or webElement
        """
        if str(type(xpath)) != "<class 'selenium.webdriver.remote.webelement.WebElement'>":
            xpath = self.get_element(xpath)
        xpath.submit()

    def js(self, scr):
        """
        封装执行JS的方法
        :param scr: JS语句
        :return: JS语句执行结果
        """
        return self.driver.execute_script(scr)

    def get_attribute(self, xpath, attribute):
        """
        封装获取元素属性的方法
        :param xpath: 定位信息，xpath or webElement
        :param attribute: 元素的属性name
        :return: 返回对象属性的value
        """

        if str(type(xpath)) != "<class 'selenium.webdriver.remote.webelement.WebElement'>":
            xpath = self.get_element(xpath)
        return xpath.get_attribute(attribute)

    def get_text(self, xpath):
        """
        封装获取元素text的方法
        :param xpath: 定位信息，xpath or webelement
        :return: 返回文本信息
        """
        if str(type(xpath)) != "<class 'selenium.webdriver.remote.webelement.WebElement'>":
            xpath = self.get_element(xpath)
        return xpath.text

    def get_display(self, xpath):
        """
        封装获取元素是否可见的方法
        :param xpath: 定位信息，xpath or webelement
        :return: 可见返回true，否则抛异常
        """
        if str(type(xpath)) != "<class 'selenium.webdriver.remote.webelement.WebElement'>":
            xpath = self.get_element(xpath)
        return xpath.is_displayed()

    def get_enable(self, xpath):
        """
        封装获取元素是否enabled的方法
        :param xpath: 定位信息，xpath or webelement
        :return: enabled返回true，否则返回false
        """
        if str(type(xpath)) != "<class 'selenium.webdriver.remote.webelement.WebElement'>":
            xpath = self.get_element(xpath)
        return xpath.is_enabled()

    def get_select(self, xpath):
        """
        封装获取元素是否的方选中的方法
        :param xpath: 定位信息，xpath or webelement
        :return: select返回true，否则返回false
        """
        if str(type(xpath)) != "<class 'selenium.webdriver.remote.webelement.WebElement'>":
            xpath = self.get_element(xpath)
        return xpath.is_selected()

    def get_title(self):
        """封装获取当前窗口的title方法"""
        return self.driver.title

    def get_window_img(self, file_path):
        """获取当前窗口截图的方法"""

        self.driver.get_screenshot_as_file(file_path)

    def get_screenshot(self, filename):
        """
        获取当前窗口截图的方法
        :param filename: 需要截图的文件名，截图生成为PNG格式，并保存再根目录中的image下
        :return: 返回截图的绝对路径
        """
        base_dir = os.path.dirname(__file__)
        base_dir = str(base_dir)
        base = base_dir.split('public')[0]
        base = base + "screenshot\\"
        path = filename + ".png"
        all_path = base + path
        self.driver.get_screenshot_as_file(all_path)
        return all_path

    def wait(self, secs):
        """
        封装显示等待的方法
        :param secs: 等待时间，单位是秒
        """
        self.driver.implicitly_wait(secs)

    def switch_to_frame(self, xpath):
        """
        封装切换frame的方法
        :param xpath: 定位信息，xpath or webelement
        """
        iframe_el = self.get_element(xpath)
        self.driver.switch_to.frame(iframe_el)

    def switch_to_frame_out(self):
        """返回默认frame，与switch_to_frame对应"""
        self.driver.switch_to.default_content()

    def switch_to_window(self, index):
        """
        封装切换window的方法,切换到最新的窗口
        :param index: 窗口handles list的index
        """
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[index])

    def screenshot_cp(self, imgelement, imgpath):
        """
        封装元素截图后与预期图对比的方法
        :param imgelement: 对比的元素对象
        :param imgpath: 对比的原图路径
        :return: 返回0.0比对成功，否则比对失败
        """
        base_dir = os.path.dirname(os.path.dirname(__file__))
        base_dir = str(base_dir)
        file_path = base_dir + "\\web_image\\test.png"
        file_path1 = base_dir + "\\web_image\\test1.png"
        imgpath = base_dir + "\\web_image\\" + imgpath
        # 截取当前网页，该网页有我们需要的验证码
        self.get_window_img(file_path)
        # 获取验证码x,y轴坐标
        location = imgelement.location
        # 获取对象的长宽
        size = imgelement.size
        # 写成我们需要截取的位置坐标
        rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']), int(location['y'] + size[
            'height']))
        # 打开截图
        im = Image.open(file_path)
        # 使用Image的crop函数，从截图中再次截取我们需要的区域
        frame4 = im.crop(rangle)
        frame4.save(file_path1)

        imgpath = base_dir + imgpath
        image1 = Image.open(imgpath)
        image2 = Image.open(file_path1)

        h1 = image1.histogram()
        h2 = image2.histogram()

        # sqrt:计算平方根，reduce函数：前一次调用的结果和sequence的下一个元素传递给operator.add
        # operator.add(x,y)对应表达式：x+y
        # 这个函数是方差的数学公式：S^2= ∑(X-Y) ^2 / (n-1)
        result = math.sqrt(reduce(operator.add,  list(map(lambda a, b: (a-b)**2, h1, h2)))/len(h1))
        # 如果两张图片完全相等，则返回结果为浮点类型“0.0”，如果不相同则返回结果值越大。
        return result

    def wait_windows(self, window_name, sec=10):
        """
        警视专用API，不适用其他项目
        封装等待window出现，以title为判断条件，默认10秒,10m后如果找到对应窗口返回true，找不到返回false
        'historyVideoPlayer': 历史视频播放窗口,
        'realtimeVideoPlayer': 直播播放窗口,
        'videoBackingCalling': 视频回传呼叫窗口,
        'videoBackingPlaying': 视频回传播放窗口,
        'picture': ''
        :param window_name: 窗口名称
        :param sec: 等待时间
        :return:
        """
        chatjs = "return document.title"
        js = "return window.videoWindowObj." + window_name
        if window_name != "historyVideoPlayer" and window_name != "realtimeVideoPlayer" and window_name != \
                "videoBackingCalling" and window_name != "videoBackingPlaying":
            handles = self.get_window_handles()
            for i in range(0, sec):
                time.sleep(1)
                for handle in handles:
                    self.driver.switch_to.window(handle)
                    if self.js(chatjs) != window_name:
                        pass
                    else:
                        return True
            return False
        else:
            self.switch_to_window(0)
            for i in range(0, sec):
                time.sleep(1)
                if self.js(js) == "":
                    pass
                else:
                    return True
            return False

    def get_elsize(self, xpath):
        """
        封装获取元素的size
        :param xpath: 定位信息，xpath or webelement
        :return: 返回元素size{'height':'',''width:''}
        """
        if str(type(xpath)) != "<class 'selenium.webdriver.remote.webelement.WebElement'>":
            xpath = self.get_element(xpath)
        return xpath.size

    def get_winsize(self):
        """
        封装获取窗口大小的方法
        NW的window有一层壳，获取窗口size需要用到JS
        :return: 返回窗口size{'height':'',''width:''}
        """
        size = {'width': '', 'height': ''}
        height = "var a = window.require('nw.gui').Window.get().height;return a"
        width = "return window.require('nw.gui').Window.get().width"
        size['height'] = self.js(height)
        size['width'] = self.js(width)
        return size

    def get_winlocation(self):
        """
        封装窗口的位置坐标方法
        NW的window有一层壳，获取窗口location需要用到JS
        :return: 返回窗口location{'height':'',''width:''}
        """
        location = {'x': '', 'y': ''}
        x = "return window.require('nw.gui').Window.get().x"
        y = "return window.require('nw.gui').Window.get().y"
        location['x'] = self.js(x)
        location['y'] = self.js(y)
        return location

    def get_window_handles(self):
        """
        封装获取window_handles方法
        :return: 返回所有window的handle
        """
        return self.driver.window_handles

    def open_new_window(self, sec=30):
        """
        封装判断是否打开了新window
        :param sec: 等待时间，单位是秒
        :return: 有新window返回true，否则返回false
        """
        return WebDriverWait(self.driver, sec, 1).until(ec.new_window_is_opened)

    def windows_number(self, num, sec=30):
        """
        封装判断等待windows数量为指定值
        :param num: window的数量
        :param sec: 等待时间，单位是秒
        :return: 有指定数量window出现返回true，否则返回false
        """
        return WebDriverWait(self.driver, sec, 1).until(ec.number_of_windows_to_be, num)

    @staticmethod
    def win32_find_win(class_name=None, window_name=None):
        """
        封装win32gui的findWindow方法
        :param class_name: 窗口的class name，如#32770
        :param window_name: 窗口的title，如"记事本"
        :return:: 找到返回窗口句柄
        """
        return win32gui.FindWindow(class_name, window_name)

    @staticmethod
    def win32_find_winex(hwnd=0, hwnd_after=0, class_name=None, window_name=None):
        """
        封装win32gui的findwindow方法
        :param hwnd: 若不为0，则搜索句柄为hwndParent窗体的子窗体
        :param hwnd_after:若不为0，则按照z-index的顺序从hwndChildAfter向后开始搜索子窗体，否则从第一个子窗体开始搜索
        :param class_name: 窗口的class name，如#32770
        :param window_name: 窗口的title，如"记事本"
        :return: 找到返回主窗口中的子窗体
        """
        return win32gui.FindWindowEx(hwnd, hwnd_after, class_name, window_name)

    @staticmethod
    def win32_sendmessage(hwnd, msg, wparam=None, lparam=None):
        """
        封装win32gui对控件发送消息方法
        :param hwnd: 接收消息的窗体句柄
        :param msg: 要发送的消息
        :param wparam:取决于消息类型
        :param lparam:取决于消息类型
        """
        win32gui.SendMessage(hwnd, msg, wparam, lparam)

    @staticmethod
    def input_text_wm(hwnd, text):
        """
        封装win32向控件输入文本的方法
        :param hwnd: 控件的句柄
        :param text: 要输入的文本信息
        """
        win32gui.SendMessage(hwnd, win32con.WM_SETTEXT, None, text)

    @staticmethod
    def click_button_wm(hwnd, hwnd_button):
        """
        封装win32点击按钮的方法
        :param hwnd: 主窗口句柄
        :param hwnd_button: 按钮句柄
        """
        win32gui.SendMessage(hwnd, win32con.WM_COMMAND, 1, hwnd_button)

    @staticmethod
    def get_textlen_wm(hwnd):
        """
        封装win32获取文本长度方法
        :param hwnd: 控件句柄
        :return: 文本长度
        """
        return win32gui.SendMessage(hwnd, win32con.WM_GETTEXTLENGTH)

    def get_text_wm(self, hwnd):
        """
        封装win32获取文本方法
        :param hwnd: 控件句柄
        :return: 文本信息
        """
        buffer = '0' * 255
        length = self.get_textlen_wm(hwnd) + 1  # 获取edit控件文本长度
        win32gui.SendMessage(hwnd, win32con.WM_GETTEXT, length, buffer)  # 读取文本
        return buffer[:length - 1]

    @staticmethod
    def close_window_wm(hwnd):
        """
        封装win32关闭窗口的方法
        :param hwnd: 窗口句柄
        """
        win32gui.SendMessage(hwnd, win32con.WM_CLOSE, 0, 0)

    @staticmethod
    def keybd_event_wm(bvk, bscan, dwflags=0, dwextrainfo=0):
        """
        封装win32api模拟键盘事件方法
        :param bvk: 键盘按键代码
        :param bscan: 硬件扫描代码
        :param dwflags: 标志指定各种功能选项
        :param dwextrainfo: 与击键相关的附加数据
        附个键位码表：
    字母和数字键     数字小键盘的键       功能键         其它键
    键   键码        键   键码            键   键码      键      键码
      A   65         0   96                 F1   112     Backspace    8
      B   66         1   97                 F2   113     Tab       9
      C   67         2   98                 F3   114     Clear      12
      D   68         3   99                 F4   115     Enter      13
      E   69         4   100                F5   116     Shift      16
      F   70         5   101                F6   117     Control     17
      G   71         6   102                F7   118     Alt       18
      H   72         7   103                F8   119     Caps Lock    20
      I   73         8   104                F9   120     Esc       27
      J   74         9   105                F10  121     Spacebar    32
      K   75         *   106                F11  122     Page Up     33
      L   76         +   107                F12  123     Page Down    34
      M   77         Enter 108                           End       35
      N   78         -   109                             Home      36
      O   79         .   110                             Left Arrow   37
      P   80         /   111                             Up Arrow    38
      Q   81                                             Right Arrow   39
      R   82                                             Down Arrow    40
      S   83                                             Insert      45
      T   84                                             Delete      46
      U   85                                             Help       47
      V   86                                             Num Lock     144
      W   87
      X   88
      Y   89
      Z   90
      0   48
      1   49
      2   50
      3   51
      4   52
      5   53
      6   54
      7   55
      8   56
      9   57
        """
        win32api.keybd_event(bvk, bscan, dwflags, dwextrainfo)
        win32api.keybd_event(bvk, bscan, win32con.KEYEVENTF_KEYUP, dwextrainfo)

    def mouse_left_click_wm(self, dx=None, dy=None, times=1):
        """
        封装win32api模拟鼠标左键方法
        :param dx: 鼠标的水平位置
        :param dy: 鼠标的垂直位置
        :param times:点击次数
        """
        self.mouse_move_wm(dx, dy)
        time.sleep(0.05)
        while times:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            times -= 1

    def mouse_right_click_wm(self, dx=None, dy=None):
        """
        封装win32api模拟鼠标右键方法
        :param dx: 鼠标的水平位置
        :param dy: 鼠标的垂直位置
        """
        self.mouse_move_wm(dx, dy)
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    @staticmethod
    def mouse_move_wm(dx, dy):
        """
        封装鼠标移动方法
        :param dx: 鼠标的水平位置
        :param dy: 鼠标的垂直位置
        """
        if dx is not None and dy is not None:
            point = (dx, dy)
            win32api.SetCursorPos(point)

    @staticmethod
    def get_mouse_position_wm():
        """
        封装获取鼠标当前位置方法
        :return:  返回x，y
        """
        pos = win32api.GetCursorPos()
        pos[0] = int(pos[0])
        pos[1] = int(pos[1])
        return pos

    def assert_in(self, test1, test2):
        """2次封装包含断言，让其断言不通过截图"""
        try:
            assert test1 in test2, "%s not found in %s" % (repr(test1), repr(test2))
        except AssertionError as msg:
            f = self.get_screenshot(str(inspect.stack()[1][3]))
            a = open(f, 'rb').read()
            allure.MASTER_HELPER.attach('screenshot', a, type=allure.MASTER_HELPER.attach_type.PNG)
            raise AssertionError(msg)

    def assert_not_in(self, test1, test2):
        """2次封装非包含断言，让其断言不通过截图"""
        try:
            assert test1 not in test2, "%s unexpectedly found in  %s" % (repr(test1), repr(test2))
        except Exception as msg:
            f = self.get_screenshot(str(inspect.stack()[1][3]))
            a = open(f, 'rb').read()
            allure.MASTER_HELPER.attach('screenshot', a, type=allure.MASTER_HELPER.attach_type.PNG)
            raise AssertionError(msg)

    def assert_equal(self, test1, test2):
        """2次封装相等断言，让其断言不通过截图"""
        try:
            assert test1 == test2, "%s != %s" % (repr(test1), repr(test2))
        except Exception as msg:
            f = self.get_screenshot(str(inspect.stack()[1][3]))
            a = open(f, 'rb').read()
            allure.MASTER_HELPER.attach('screenshot', a, type=allure.MASTER_HELPER.attach_type.PNG)
            raise AssertionError(msg)

    def assert_not_equal(self, test1, test2):
        """2次封装不相等断言，让其断言不通过截图"""
        try:
            assert test1 != test2, "%s != %s" % (repr(test1), repr(test2))
        except Exception as msg:
            f = self.get_screenshot(str(inspect.stack()[1][3]))
            a = open(f, 'rb').read()
            allure.MASTER_HELPER.attach('screenshot', a, type=allure.MASTER_HELPER.attach_type.PNG)
            raise AssertionError(msg)

    def assert_true(self, test):
        """2次封装为真断言，让其断言不通过截图"""
        try:
            assert test is True, "%s is not true" % str(test)
        except Exception as msg:
            f = self.get_screenshot(str(inspect.stack()[1][3]))
            a = open(f, 'rb').read()
            allure.MASTER_HELPER.attach('screenshot', a, type=allure.MASTER_HELPER.attach_type.PNG)
            raise AssertionError(msg)

    def assert_false(self, test):
        """2次封装为真断言，让其断言不通过截图"""
        try:
            assert test is False, "%s is not false" % str(test)
        except Exception as msg:
            f = self.get_screenshot(str(inspect.stack()[1][3]))
            a = open(f, 'rb').read()
            allure.MASTER_HELPER.attach('screenshot', a, type=allure.MASTER_HELPER.attach_type.PNG)
            raise AssertionError(msg)

    @staticmethod
    def read_data_yaml():
        """封装读取yaml文件操作"""
        base_dir = os.path.dirname(__file__)
        base = str(base_dir).split("public")[0]
        yaml_file = base + "test_case\\data.yaml"
        f = open(yaml_file, 'r')
        info = f.read()
        data = yaml.load(info)
        f.close()
        return data


