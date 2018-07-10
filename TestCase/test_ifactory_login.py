# coding=utf-8
'''
Created on 2018-6-27
@author: suchao
Project:使用unittest框架编写测试用例,实现GF-1匀光匀色流程创建。
'''
import unittest
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from TestPage.ifactory_homepage import IfactoryHomePage
from TestPage.ifactory_login import IfactoryLoginPage
from TestPage.ifactory_imageprocess import ImageProcessPage
from TestPage.browser_engine import BrowserEngine

from TestPage.ifactory_task_manager_gf1 import Gf1TaskManagerPage


# 解析流程所使用的(状态)图片，例如: ../../images/flow/state/wanchen.png
def get_process_state(path):
    result = path.split('state/')
    state = result[1].split('.')[0]
    return state


class CaseLoginICenter(unittest.TestCase):

    def setUp(self):
        self.driver = BrowserEngine(self).get_browser()  # 启动浏览器

        # ip = "http://192.168.31.167:8283"
        ip = "http://192.168.159.133:8283"
        self.login_url = ip + "/pixelfactory/views/index.html"
        self.homepage_url = ip + "/pixelfactory/views/task/index.html"
        self.image_process_url = ip + "/pixelfactory/views/task/flows.html"
        self.add_task_gf1_url = ip + "/pixelfactory/views/task/task.html?id=46022e53ed064c75866be6701b67138f"

        # data
        self.name = "test_task01"  # 名称
        self.src_cor = "GCS WGS 1984"  # 源坐标系，已设置缺省值GCS WGS 1984
        self.trg_cor = "GCS WGS 1984"  # 目的坐标系，已设置缺省值GCS WGS 1984
        self.org_path = "/home/data/3j-GF1/input"  # 原始影像路径

    # 用例执行体
    def test_login_liucheng(self):
        u"""测试登录用例"""
        # 声明LoginPage类对象
        login_page = IfactoryLoginPage(self.driver, self.login_url, "Login")
        # 调用打开页面组件
        login_page.open()
        # 点击登录按钮
        login_page.click_login()
        time.sleep(1)

        process_result= True
        self.assertTrue(process_result, msg="流程进行失败")

        time.sleep(10)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
