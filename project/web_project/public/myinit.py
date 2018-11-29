# -*- coding: utf-8 -*-
import allure
from ..pages.login_page import Login
from .wd_public import WDPublic


class MyTest:

    def setup(self):
        with allure.MASTER_HELPER.step("启动应用"):
            self.driver = WDPublic(self.path)
            self.driver.wait(30)

        self.login = Login(self.driver)

    def teardown(self):
        with allure.MASTER_HELPER.step("退出应用"):
            self.driver.quit()


