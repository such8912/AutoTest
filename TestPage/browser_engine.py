# coding = utf-8
from selenium import webdriver


class BrowserEngine(object):
    def __init__(self, driver):
        self.driver = driver

    # 默认使用Chrome浏览器测试，如需要其他浏览器引擎，则修改
    browser_type = "Chrome"

    def get_browser(self):
        if self.browser_type == "Chrome":
            driver = webdriver.Chrome()
        elif self.browser_type == "Firefox":
            driver = webdriver.Firefox()
        elif self.browser_type == "IE":
            driver = webdriver.Ie()
        else:
            driver = webdriver.Chrome()

        driver.maximize_window()
        driver.implicitly_wait(10)

        return driver
