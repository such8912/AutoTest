# coding=utf-8
'''
Created on 2016-8-21
@author: suchao
Project:页面基本操作方法：如open，input_username，input_password，click_submit
'''
from selenium.webdriver.common.by import By
from BasePage import BasePage


# 继承BasePage类
class IfactoryLoginPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    login_loc = ('XPATH', '//*[@id="change_img"]')

    # 操作
    # 通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 打开网页
    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url, self.pagetitle)

    # 点击登陆
    def click_login(self):
        self.find_element(self.login_loc).click()
