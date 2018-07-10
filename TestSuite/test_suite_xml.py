# coding=utf-8
import unittest, time
import sys, os
# 需要将HTMLTestRunner.py放在C:\Python27\Lib下
from HTMLTestRunner import HTMLTestRunner

from xmlrunner import xmlrunner

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

    # runner = xmlrunner.XMLTestRunner(output='report')#输入到report文件夹中
    runner = xmlrunner.XMLTestRunner(output=report_path + "\\")#输入到eport文件夹中
    report_path + "\\"
    runner.run(suite)

