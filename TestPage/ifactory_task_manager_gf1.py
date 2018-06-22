# coding=utf-8
'''
Created on 2016-8-21
@author: suchao
Project:定义GF-1任务管理流程影像处理页面相关操作
'''
from selenium.webdriver.common.by import By
from BasePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


# 继承BasePage类
class Gf1TaskManagerPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    addtask_loc = ('XPATH', '//*/img[@class="taskImg"]')
    addtask_nav_loc = ('XPATH', '//*[@id="taskUi"]')
    task_name_loc = ('XPATH', '//*[@id="name"]')
    src_cor_loc = ('XPATH', '//*[@id="sourceCoord"]')
    trg_cor_loc = ('XPATH', '//*[@id="targetCoord"]')
    new_folder_loc = ('XPATH', '//*[@id="newFolder"]')
    origin_image_loc = ('XPATH', '//*[@id="folderName"]')
    button_next_loc = ('XPATH', '//*[@id="tab-content-id"]/ul/li[4]/a')

    # 操作
    # 通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 打开网页
    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url, self.pagetitle)

    # 点击新增任务【+】
    def click_gf1_addtask(self):
        self.find_element(self.addtask_loc).click()

    # 点击新增任务【+】旁边的空白处，先找到该层元素，再去点新增任务【+】
    def click_gf1_addtask_nav(self):
        self.find_element(self.addtask_nav_loc).click()

    # 输入名称：调用send_keys对象
    def input_task_name(self, name):
        self.find_element(self.task_name_loc).clear()
        self.find_element(self.task_name_loc).send_keys(name)

    # 选择源坐标系
    def select_src_cor(self, text):
        if text != "GCS WGS 1984" and text != "1954北京" and text != "1980西安" and text != "CGCS2000":
            text_input = "GCS WGS 1984"
        else:
            text_input = text
        elem = self.find_element(self.src_cor_loc)
        Select(elem).select_by_visible_text(text_input)

    # 选择目的坐标系
    def select_trg_cor(self, text):
        if text != "GCS WGS 1984" and text != "1954北京" and text != "1980西安" and text != "CGCS2000":
            text_input = "GCS WGS 1984"
        else:
            text_input = text
        elem = self.find_element(self.trg_cor_loc)
        Select(elem).select_by_visible_text(text_input)

    # 输入原始影像路径
    def input_origin_path(self, driver, text):
        # 通过JS代码去掉disabled属性，这样就可以直接填值了
        driver.execute_script('document.getElementById("folderName").removeAttribute("disabled");')
        self.find_element(self.origin_image_loc).clear()
        self.find_element(self.origin_image_loc).send_keys(text)

    # 输入工程路径
    def input_prj_path(self, text):
        self.find_element(self.new_folder_loc).clear()
        self.find_element(self.new_folder_loc).send_keys(text)

    # 点击下一步
    def click_button_next(self):
        self.find_element(self.button_next_loc).click()

