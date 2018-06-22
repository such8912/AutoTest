# coding = utf-8
from selenium import webdriver


class BrowserEngine(object):
    def __init__(self, driver):
        self.driver = driver

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
