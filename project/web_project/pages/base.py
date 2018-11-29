# -*- coding: utf-8 -*-


class Page(object):
    """页面基础类，用于所有页面继承"""
    def __init__(self, selenium_driver, parent=None):
        self.driver = selenium_driver
        self.timeout = 15
        self.parent = parent
