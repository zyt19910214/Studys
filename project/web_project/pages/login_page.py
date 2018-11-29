# -*- coding: utf-8 -*-
from time import sleep
import allure
from .base import Page


class Login(Page):
    """用户登录页面"""
    username = 'admin20'
    password = '111111'

    # 封装登录
    def login(self, name=username, pw=password):
        self.input_login_username(name)
        sleep(1)
        self.input_login_password(pw)
        sleep(1)
        self.click_login_loginbutton()

    # 登录页面用户名输入框
    login_username = "name=>username"

    def input_login_username(self, username):
        with allure.MASTER_HELPER.step('清空用户名输入框'):
            self.driver.clear(self.login_username)
        with allure.MASTER_HELPER.step('用户名输入框输入：' + username):
            self.driver.input(self.login_username, username)

    # 登录页面密码输入框
    login_password = "name=>password"

    def input_login_password(self, password):
        with allure.MASTER_HELPER.step('清空密码输入框'):
            self.driver.clear(self.login_password)
        with allure.MASTER_HELPER.step('密码输入框输入：' + password):
            self.driver.input(self.login_password, password)

    def get_login_password_attribute(self, attribute):
        with allure.MASTER_HELPER.step('获取登录密码框的属性：' + attribute):
            return self.driver.get_attribute(self.login_password, attribute)

    # 登录页面密码眼睛按钮
    login_show_password = "//img[@oncopy='return false']"

    def click_login_showpassword(self):
        with allure.MASTER_HELPER.step('点击show按钮'):
            self.driver.click(self.login_show_password)

    # 登录页面登录按钮
    login_loginbutton = "class=>grey-button"

    def click_login_loginbutton(self):
        with allure.MASTER_HELPER.step('点击登录按钮'):
            self.driver.click(self.login_loginbutton)

    def get_login_loginbutton_attribute(self, attribute):
        with allure.MASTER_HELPER.step('获取登录按钮的属性：' + attribute):
            return self.driver.get_attribute(self.login_loginbutton, attribute)

    # 登录页面忘记密码
    login_forget_password = "//div[@class='forget-password']/p"

    def click_login_forgetpassword(self):
        with allure.MASTER_HELPER.step('点击忘记密码'):
            self.driver.click(self.login_forget_password)

    # 登录页面，错误提示
    login_errorinfo = "class=>error"

    def login_errorinfo_text(self, text):
        with allure.MASTER_HELPER.step('等待%s提示信息' % text):
            return self.driver.toast_msg_text(self.login_errorinfo, text)

    # toast-msg
    toast_msg = "//div[@id='toastMessage']/div/span"

    def toast_msg_text(self, msg):
        with allure.MASTER_HELPER.step('获取toast提示信息：%s' % msg):
            return self.driver.toast_msg_text(self.toast_msg, msg)
