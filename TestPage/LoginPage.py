# coding=utf-8
'''
Created on 2016-8-21
@author: suchao
Project:页面基本操作方法：如open，input_username，input_password，click_submit
'''
from selenium.webdriver.common.by import By
from BasePage import BasePage


# 继承BasePage类
class LoginPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    username_loc = ('XPATH', '//*[@id="app"]/div/div/form/div[1]/div/div/input')
    password_loc = ('XPATH', '//*[@id="app"]/div/div/form/div[2]/div/div/input')
    submit_loc = ('XPATH', '//*[@id="app"]/div/div/form/div[3]/div/button/span')

    # 操作
    # 通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 打开网页
    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url, self.pagetitle)

    # 输入用户名：调用send_keys对象，输入用户名
    def input_username(self, username):
        self.find_element(self.username_loc).clear()
        self.find_element(self.username_loc).send_keys(username)
        #self.send_keys(self.find_element(self.username_loc),username) #此种写法不清晰

    # 输入密码：调用send_keys对象，输入密码
    def input_password(self, password):
        self.find_element(self.password_loc).clear()
        self.find_element(self.password_loc).send_keys(password)

    # 点击登录：调用send_keys对象，点击登录
    def click_submit(self):
        self.find_element(self.submit_loc).click()
