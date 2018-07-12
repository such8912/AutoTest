# coding=utf-8
'''
Created on 2018-6-27
@author: suchao
Project:使用unittest框架编写测试用例,实现GF-1匀光匀色流程创建。
'''
import unittest
import time
import random

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


# 产生一个长度为8的随机字符串
def random_str8():
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sa = []
    for i in range(8):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    print salt
    return salt


class CaseIFactory(unittest.TestCase):

    def setUp(self):
        self.driver = BrowserEngine(self).get_browser()  # 启动浏览器

        ip = "http://192.168.48.110:8283"
        # ip = "http://192.168.159.133:8283"
        self.login_url = ip + "/pixelfactory/views/index.html"
        self.homepage_url = ip + "/pixelfactory/views/task/index.html"
        self.image_process_url = ip + "/pixelfactory/views/task/flows.html"
        self.add_task_gf1_url = ip + "/pixelfactory/views/task/task.html?id=46022e53ed064c75866be6701b67138f"

        # data
        # self.name = "test_task101"  # 名称
        self.name = random_str8()
        self.src_cor = "GCS WGS 1984"  # 源坐标系，已设置缺省值GCS WGS 1984
        self.trg_cor = "GCS WGS 1984"  # 目的坐标系，已设置缺省值GCS WGS 1984
        self.org_path = "/home/data/3j-GF1/input"  # 原始影像路径

    # 用例执行体
    def test_gf1_ygys(self):
        u"""测试增加匀光匀色流程用例"""
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

        # 在影像处理流程页面，双击“GF1遥感卫星影像匀光匀色处理流程”
        image_process_page = ImageProcessPage(self.driver, self.image_process_url, "GeoVisFactory FlowsPage")
        image_process_page.click_gf1_ygys()
        time.sleep(1)

        # 点击新增任务
        addtask_page = Gf1TaskManagerPage(self.driver, self.add_task_gf1_url, "EditTask")
        # addtask_page.click_gf1_addtask_nav()
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

        # 点击完成后需动态新的任务出现在页面上（共等待10秒，每隔1秒检索一次，否则抛异常）
        try:
            WebDriverWait(self.driver, 10, 1).until(lambda driver: driver.find_element_by_xpath(
                '//label[text()="%s" ]' % self.name).is_displayed())
        except:
            print ("element can not find")

        # 点击开始任务
        time.sleep(1)
        addtask_page.click_begin_task()
        time.sleep(2)

        # 点击确认开始
        addtask_page.click_ok_button()

        # 找到第一个流程，然后鼠标悬停上去，使下方的流程图状态显示出来
        elem = self.driver.find_element_by_xpath('//*[@id="taskUi"]/li[1]')
        ActionChains(self.driver).move_to_element(elem).perform()
        time.sleep(1)

        # 获取匀光匀色的状态
        # xpath1 = '//div[@id="flowUi"]/div[@id="state_decide8"]/img[1]'
        # last_path = self.driver.find_element_by_xpath(xpath1).get_attribute("src")
        # result = get_process_state(last_path)

        result8 = "zhunbei"
        process_result = False
        while result8 == "zhunbei" or result8 == "yunxin":
            # 每隔5秒获取一次匀光匀色的结果状态，流程是否成功，只以匀光匀色的最终状态为准
            # （1）如果匀光匀色最终状态为wancheng，则证明流程成功完成；
            # （2）如果匀光匀色最终状态为zhunbei，则证明流程成功还未完成，需去判断前面的步骤是否产生错误；如果前面的步骤产生了错误，
            #      则说明整个流程失败
            # （3）如果匀光匀色最终状态为cuowu,则说明恰好流程在匀光匀色出错，流程错误结束。
            time.sleep(5)
            xpath8 = '//div[@id="flowUi"]/div[@id="state_decide8"]/img[1]'
            result8 = get_process_state(self.driver.find_element_by_xpath(xpath8).get_attribute("src"))
            print u"获取到的匀光匀色的状态为：" + result8
            time.sleep(1)

            if result8 == "zhunbei":  # 如果匀光匀色是准备，可能有两种情况，1.前面已经有流程错误；2.流程还未走到匀光匀色

                # 判断"数据组织"状态，如果为错误，则流程结束
                xpath3 = '//div[@id="flowUi"]/div[@id="state_decide3"]/img[1]'
                result3 = get_process_state(self.driver.find_element_by_xpath(xpath3).get_attribute("src"))
                if result3 == "cuowu":
                    print "result3 error"
                    process_result = False
                    break

                # 判断"并行"状态，如果为错误，则流程结束
                xpath4 = '//div[@id="flowUi"]/div[@id="state_decide4"]/img[1]'
                result4 = get_process_state(self.driver.find_element_by_xpath(xpath4).get_attribute("src"))
                if result4 == "cuowu":
                    print "result4 error"
                    process_result = False
                    break

                # 判断"正射校正"状态，如果为错误，则流程结束
                xpath5 = '//div[@id="flowUi"]/div[@id="state_decide5"]/img[1]'
                result5 = get_process_state(self.driver.find_element_by_xpath(xpath5).get_attribute("src"))
                if result5 == "cuowu":
                    print u"正射校正状态错误"
                    print "result5 error"
                    process_result = False
                    break

                # 判断"正射校正"状态，如果为错误，则流程结束
                xpath6 = '//div[@id="flowUi"]/div[@id="state_decide6"]/img[1]'
                result6 = get_process_state(self.driver.find_element_by_xpath(xpath6).get_attribute("src"))
                if result6 == "cuowu":
                    print u"正射校正状态错误"
                    process_result = False
                    break

                # 判断"GS融合"状态，如果为错误，则流程结束
                xpath11 = '//div[@id="flowUi"]/div[@id="state_decide11"]/img[1]'
                result11 = get_process_state(self.driver.find_element_by_xpath(xpath11).get_attribute("src"))
                if result11 == "cuowu":
                    print u"GS融合状态错误"
                    process_result = False
                    break

            elif result8 == "wanchen":  # 如果匀光匀色是完成状态，则证明流程彻底结束
                print u"流程完成了"
                process_result = True
                break
            elif result8 == "cuowu":
                print u"匀光匀色流程流程错误"  # 如果匀光匀色是错误状态，则证明该步骤产生错误
                process_result = False
                break
            else:  # 匀光匀色状态若是yunxin，则不必理会，继续循环判断
                continue

        print u"进入到断言前process_result的值:" + str(process_result)
        self.assertTrue(process_result, msg="流程进行失败")

        time.sleep(10)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
