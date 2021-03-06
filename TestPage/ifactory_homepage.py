# coding=utf-8
'''
Created on 2016-8-21
@author: suchao
Project:定义ifactoty HomePage相关操作
'''
from selenium.webdriver.common.by import By
from BasePage import BasePage


# 继承BasePage类
class IfactoryHomePage(BasePage):
    # 定位器，通过元素属性定位元素对象
    image_process_flow_loc = ('XPATH', '//*[@id="bs-example-navbar-collapse-1"]/ul[1]/li[4]/a')

    # 操作
    # 通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 打开网页
    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url, self.pagetitle)

    # 点击GF-1匀光匀色
    def click_imageprocessflow(self):
        self.find_element(self.image_process_flow_loc).click()
