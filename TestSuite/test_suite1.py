# coding=utf-8
import unittest, time
import sys, os
from HTMLTestRunner import HTMLTestRunner
from os import path

reload(sys)
sys.setdefaultencoding('utf8')

# 获取工程路径和测试报告路径
project_path = os.path.dirname(os.path.realpath(__file__))
project_path = os.path.dirname(os.path.realpath(project_path))
print project_path
report_path = os.path.join(project_path, 'Report')
print report_path


# project_path = "C:\\Users\\user\\PycharmProjects\\AutoTest\\"


# ---将用例添加到测试套件---
def creatsuite():
    testunit = unittest.TestSuite()
    test_dir = project_path + "\TestCase"
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_*.py", top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTest(test_case)
            print (testunit)
    return testunit


if __name__ == "__main__":
    suite = creatsuite()
    # runner = unittest.TextTestRunner()
    # 定义测试报告存放位置
    # 使用HTMLTestRunner生成结果报告到'Report'文件夹下，名为当前时间+result.html
    now_time = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = report_path + "\\"+ 'TestResult' + now_time + '.html'  # 假设已新建report文件
    # 设置HTML的title和概括
    f = open(filename, 'wb')
    runner = HTMLTestRunner(stream=f, title='测试报告标题', description='报告概括')
    runner.run(suite)
    f.close()
