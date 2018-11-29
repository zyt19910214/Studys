# -*- coding: utf-8 -*-
from time import sleep
import allure
import pytest
from project.web_project.public.myinit import MyTest
from project.web_project.public.wd_public import WDPublic


@allure.MASTER_HELPER.feature(u"登录功能")
class WTestLogin(MyTest):
    u"""PoliceVP登录测试"""

    data = WDPublic.read_data_yaml()
    path = data['base']['path']
    report = data['base']['report']
    APP = data['base']['APP']
    OS = data['base']['OS']
    username = data['loginuser']['username']
    password = data['loginuser']['password']
    wrongPassword = data['loginuser']['wrongPW']
    wrongPW_msg = data['loginuser']['wrongPWMsg']
    wrongUserN_msg = data['loginuser']['wrongUNMsg']
    wrongUserName = data['loginuser']['wrongUN']
    Less_6_name = data['loginuser']['Less_6']
    loginbtn_attribute = data['loginpage']['loginbtnabN']
    loginbtn_attribute_ash = data['loginpage']['loginbtnabA']
    loginbtn_attribute_light = data['loginpage']['loginbtnabL']
    password_attribute = data['loginpage']['passwordN']
    password_attribute_text = data['loginpage']['passwordT']
    password_attribute_PW = data['loginpage']['passwordP']
    forget_toast_msg = data['toast']['forgetPW']

    allure.MASTER_HELPER.environment(report=report, APP=APP, OS=OS)

    @allure.MASTER_HELPER.story("正确登录")
    @allure.MASTER_HELPER.severity(allure.MASTER_HELPER.severity_level.BLOCKER)
    @allure.MASTER_HELPER.issue("http://192.168.9.240:82/pro/bug-view-30214.html")
    @allure.MASTER_HELPER.testcase("http://192.168.9.240:82/pro/bug-view-30214.html")
    @pytest.mark.parametrize("username, password", [(username, password)])
    def test_login01(self, username, password):
        """正确登录，弹出首页"""
        self.login.login(username, password)
        sleep(5)
        self.driver.assert_in(u"人员调度1111", u"人员调度")

    @allure.MASTER_HELPER.story("错误登录")
    @allure.MASTER_HELPER.severity(allure.MASTER_HELPER.severity_level.NORMAL)
    @allure.MASTER_HELPER.issue("http://192.168.9.240:82/pro/bug-view-30214.html")
    @allure.MASTER_HELPER.testcase("http://192.168.9.240:82/pro/bug-view-30214.html")
    @pytest.mark.parametrize("username, password, wrong_msg", [(username, wrongPassword, wrongPW_msg),
                                                               (wrongUserName, password, wrongUserN_msg)])
    def test_login02(self, username, password, wrong_msg):
        """错误登录，有提示信息"""
        self.login.login(username, password)
        sleep(2)
        self.driver.assert_true(self.login.login_errorinfo_text(wrong_msg))

    @allure.MASTER_HELPER.story("输入信息小于6位，登录按钮置灰")
    @allure.MASTER_HELPER.severity(allure.MASTER_HELPER.severity_level.TRIVIAL)
    @allure.MASTER_HELPER.issue("http://192.168.9.240:82/pro/bug-view-30214.html")
    @allure.MASTER_HELPER.testcase("http://192.168.9.240:82/pro/bug-view-30214.html")
    @pytest.mark.parametrize("username, password, button_attribute, button_attribute_value",
                             [(Less_6_name, password, loginbtn_attribute, loginbtn_attribute_ash),
                              (username, Less_6_name, loginbtn_attribute, loginbtn_attribute_ash),
                              (username, password, loginbtn_attribute, loginbtn_attribute_light)])
    def test_login03(self, username, password, button_attribute, button_attribute_value):
        """用户名或密码小于6位，登录按钮置灰"""
        self.login.input_login_username(username)
        sleep(1)
        self.login.input_login_password(password)
        sleep(1)
        self.driver.assert_equal(self.login.get_login_loginbutton_attribute(button_attribute), button_attribute_value)

    @allure.MASTER_HELPER.story("密码框明密文显示")
    @allure.MASTER_HELPER.severity(allure.MASTER_HELPER.severity_level.TRIVIAL)
    @allure.MASTER_HELPER.issue("http://192.168.9.240:82/pro/bug-view-30214.html")
    @allure.MASTER_HELPER.testcase("http://192.168.9.240:82/pro/bug-view-30214.html")
    @pytest.mark.parametrize("password, times, password_attribute, password_attribute_value",
                             [(password, 1, password_attribute, password_attribute_text),
                              (password, 2, password_attribute, password_attribute_PW)])
    def test_login04(self, password, times, password_attribute, password_attribute_value):
        """密码明文显示"""
        self.login.input_login_password(password)
        sleep(1)
        for i in range(times):
            self.login.click_login_showpassword()
            sleep(1)
        self.driver.assert_equal(self.login.get_login_password_attribute(password_attribute), password_attribute_value)

    @allure.MASTER_HELPER.story("忘记密码")
    @allure.MASTER_HELPER.severity(allure.MASTER_HELPER.severity_level.TRIVIAL)
    @allure.MASTER_HELPER.issue("http://192.168.9.240:82/pro/bug-view-30214.html")
    @allure.MASTER_HELPER.testcase("http://192.168.9.240:82/pro/bug-view-30214.html")
    def test_login05(self):
        """忘记密码提示"""
        self.login.click_login_forgetpassword()
        sleep(2)
        self.driver.assert_true(self.login.toast_msg_text(self.forget_toast_msg))
