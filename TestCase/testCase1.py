# coding=utf-8
'''
Created on 2016-8-13
@author: Jennifer
Project:使用unittest框架编写测试用例。
'''
import unittest
import time

from TestPage.LoginPage import LoginPage
from TestPage.browser_engine import BrowserEngine
from selenium import webdriver


class CaseLoginICenter(unittest.TestCase):
    """
          登录iCenter的case
    """

    def setUp(self):
        self.driver = BrowserEngine(self).get_browser() #启动浏览器
        # self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(30)
        self.url = "http://192.168.31.167:8283/pixelfactory/views/task/flows.html"

    # 用例执行体
    def test_login_mail(self):
        # 声明LoginPage类对象
        login_page = LoginPage(self.driver, self.url, "GeoVisFactory FlowsPage")
        # 调用打开页面组件
        login_page.open()
        # 调用用户名输入组件
        login_page.input_username(self.username)
        # 调用密码输入组件
        login_page.input_password(self.password)
        # 调用点击登录按钮组件
        login_page.click_submit()
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
