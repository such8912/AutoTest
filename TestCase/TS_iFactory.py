# coding=utf-8
'''
Created on 2016-8-13
@author: Jennifer
Project:使用unittest框架编写测试用例。
'''
import unittest
import time

from selenium.webdriver.support.wait import WebDriverWait

from TestPage.ifactory_homepage import IfactoryHomePage
from TestPage.ifactory_login import IfactoryLoginPage
from TestPage.ifactory_imageprocess import ImageProcessPage
from TestPage.browser_engine import BrowserEngine

from TestPage.ifactory_task_manager_gf1 import Gf1TaskManagerPage



class CaseLoginICenter(unittest.TestCase):
    """
          登录iCenter的case
    """

    def setUp(self):
        self.driver = BrowserEngine(self).get_browser()  # 启动浏览器

        # url
        self.login_url = "http://192.168.31.167:8283/pixelfactory/views/index.html"
        self.homepage_url = "http://192.168.31.167:8283/pixelfactory/views/task/index.html"
        self.image_process = "http://192.168.31.167:8283/pixelfactory/views/task/flows.html"
        self.addtask_gf1_url = "http://192.168.31.167:8283/pixelfactory/views/task/task.html?id=46022e53ed064c75866be6701b67138f"

        # data
        self.name = "test_task4"  # 名称
        self.src_cor = "GCS WGS 1984"  # 源坐标系，已设置缺省值GCS WGS 1984
        self.trg_cor = "GCS WGS 1984"  # 目的坐标系，已设置缺省值GCS WGS 1984
        self.org_path = "/home/data/2j-GF1/"  # 原始影像路径

    # 用例执行体
    def test_login_liucheng(self):
        # 声明LoginPage类对象
        login_page = IfactoryLoginPage(self.driver, self.login_url, "Login")
        # 调用打开页面组件
        login_page.open()
        # 点击登录按钮
        login_page.click_login()
        time.sleep(1)

        # 首页点击影像处理流程菜单
        home_page = IfactoryHomePage(self.driver, self.homepage_url, "Geovis iFactory")
        home_page.click_imageprocessflow()
        time.sleep(1)

        # 影像处理流程页面
        image_process_page = ImageProcessPage(self.driver, self.homepage_url, "GeoVisFactory FlowsPage")
        image_process_page.click_gf1_ygys()
        time.sleep(1)

        # 点击新增任务
        addtask_page = Gf1TaskManagerPage(self.driver, self.addtask_gf1_url, "EditTask")
        addtask_page.click_gf1_addtask_nav()
        addtask_page.click_gf1_addtask()
        time.sleep(1)
        # 填写任务参数
        addtask_page.input_task_name(self.name)
        addtask_page.select_src_cor(self.src_cor)
        addtask_page.select_trg_cor(self.trg_cor)
        addtask_page.input_origin_path(self.driver, self.org_path)
        addtask_page.input_prj_path(self.name)  # 工程路径新建文件夹名称与工程名保持一致
        addtask_page.click_button_next()
        time.sleep(1)

        # 使用滚动条滚动到指定位置
        addtask_page.scroll_target(self.driver, "MergeLayers521")

        # 点击完成
        addtask_page.click_button_finish()
        time.sleep(5)

        # 点击完成后需动态等待检索到【+】按钮（暂不可行）
        #WebDriverWait(self.driver,10).until(lambda driver: driver.find_element_by_xpath('//*/img[@class="taskImg"]').is_displayed())

        # 点击开始任务
        addtask_page.click_begin_task()
        time.sleep(2)

        # 点击确认开始
        addtask_page.click_ok_button()

        time.sleep(10)

        

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
