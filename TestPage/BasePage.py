# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from PIL import ImageGrab  # 截屏 pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pillow
from Log.mylog import MyLog # 日志
import time,os

cp = os.getcwd()
sp = os.path.join(cp, "screen_shot")


class BasePage(object):
    """
    BasePage
    """

    # 初始化driver、url、pagetitle
    def __init__(self, selenium_driver, base_url, page_title):
        self.base_url = base_url
        self.pagetitle = page_title
        self.driver = selenium_driver

    # 通过title断言进入的页面是否正确
    # 使用title获取当前窗口title，检查输入的title是否在当前title中，返回比较结果（True 或 False）
    def on_page(self, pagetitle):
        return pagetitle in self.driver.title

    # 打开页面，校验页面链接是否加载正确
    # 以单下划线_开头的方法，在使用import *时，该方法不会被导入，保证该方法为类私有的。
    def _open(self, url, pagetitle):
        # 使用get打开链接
        self.driver.get(url)
        self.driver.maximize_window()
        # 使用assert进行校验
        assert self.on_page(pagetitle), u"打开页面失败 %s" % url

    # 定义open方法，调用_open()进行打开链接
    def open(self):
        self._open(self.base_url, self.pagetitle)

    # 重写元素定位
    def find_element(self, element):
        try:
            type = element[0]
            value = element[1]
            print "type:" + type
            print "value:" + value
            if type == "id" or type == "ID" or type == "Id":
                WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(value).is_displayed())
                elem = self.driver.find_element_by_id(value)
            elif type == "name" or type == "NAME" or type == "Name":
                WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_name(value).is_displayed())
                elem = self.driver.find_element_by_name(value)
            elif type == "class" or type == "CLASS" or type == "Class":
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element_by_class_name(value).is_displayed())
                elem = self.driver.find_element_by_class_name(value)
            elif type == "link_text" or type == "LINK_TEXT" or type == "Link_text":
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element_by_link_text(value).is_displayed())
                elem = self.driver.find_element_by_link_text(value)
            elif type == "xpath" or type == "XPATH" or type == "Xpath":
                WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath(value).is_displayed())
                elem = self.driver.find_element_by_xpath(value)
            elif type == "css" or type == "CSS" or type == "Css":
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element_by_css_selector(value).is_displayed())
                elem = self.driver.find_element_by_css_selector(value)
        except Exception:
            # 截屏
            now_time = time.strftime("%Y-%m-%d %H_%M_%S")
            im = ImageGrab.grab()
            im.save(sp + "/" + now_time + '_error.jpg', 'jpeg')

            # 打印日志
            log = MyLog()
            log.log_writing("info", "类型为%s,值为%s的控件获取失败"%(type,value))

            # 抛异常
            raise ValueError("No such element found" + str(element))
        return elem

    def find_elements(self, element):
        """
        Find elements

        element is a set with format (identifier type, value), e.g. ('id','username')

        Usage:
        self.findElements(element)
        """
        try:
            type = element[0]
            value = element[1]
            if type == "id" or type == "ID" or type == "Id":
                WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(value).is_displayed())
                elem = self.driver.find_elements_by_id(value)
            elif type == "name" or type == "NAME" or type == "Name":
                WebDriverWait(self.driver, 10).until(lambda driver: driver.find_elements_by_name(value).is_displayed())
                elem = self.driver.find_elements_by_name(value)
            elif type == "class" or type == "CLASS" or type == "Class":
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_elements_by_class_name(value).is_displayed())
                elem = self.driver.find_elements_by_class_name(value)
            elif type == "link_text" or type == "LINK_TEXT" or type == "Link_text":
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_elements_by_link_text(value).is_displayed())
                elem = self.driver.find_elements_by_link_text(value)
            elif type == "xpath" or type == "XPATH" or type == "Xpath":
                WebDriverWait(self.driver, 10).until(lambda driver: driver.find_elements_by_xpath(value).is_displayed())
                elem = self.driver.find_elements_by_xpath(value)
            elif type == "css" or type == "CSS" or type == "Css":
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_elements_by_css_selector(value).is_displayed())
                elem = self.driver.find_elements_by_css_selector(value)
            else:
                now_time = time.strftime("%Y-%m-%d %H_%M_%S")
                im = ImageGrab.grab()
                im.save(sp + "/" + now_time + '_error.jpg', 'jpeg')
                raise NameError("Please correct the type in function parameter")
        except Exception:
            raise ValueError("No such element found" + str(element))
        return elem

    #   滚动条滚动到指定位置（调用JS方法）
    def scroll_target(self, driver, target_id):
        target = driver.find_element_by_id(target_id)
        driver.execute_script("arguments[0].scrollIntoView();", target)
