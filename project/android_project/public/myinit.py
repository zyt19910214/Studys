# -*- coding: utf-8 -*-
import allure
from test_suite.page_obj.web_page.web_loginPage import Login
from test_suite.public.web_public.web_public import WebPublic


class MyTest:

    def setup(self):
        with allure.MASTER_HELPER.step("启动应用"):
            self.driver = WebPublic(self.path)
            self.driver.wait(30)

        self.login = Login(self.driver)

    def teardown(self):
        with allure.MASTER_HELPER.step("退出应用"):
            self.driver.quit()
