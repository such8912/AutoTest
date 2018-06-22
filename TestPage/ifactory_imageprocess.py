# coding=utf-8
'''
Created on 2016-8-21
@author: suchao
Project:定义ifactoty 影像处理页面相关操作
'''
from selenium.webdriver.common.by import By
from BasePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains


# 继承BasePage类
class ImageProcessPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    yunguangyunse_loc = ('XPATH', '//*[@id="46022e53ed064c75866be6701b67138f"]/img')

    # 操作
    # 通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 打开网页
    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url, self.pagetitle)

    # 点击GF-1匀光匀色
    def click_gf1_ygys(self):
        elem = self.find_element(self.yunguangyunse_loc)
        ActionChains(self.driver).double_click(elem).perform()
