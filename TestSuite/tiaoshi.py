# coding=utf-8
from os import path
import os

# d= path.dirname(__file__)
# print d
# d1 = path.dirname(d)
# print d1
# # d2 = path.dirname(d1)
# # print d2
# report_path = os.path.join(d1,'Report')
# print report_path
project_path=os.path.dirname(os.path.realpath(__file__))
project_path=os.path.dirname(os.path.realpath(project_path))
print project_path
report_path = os.path.join(project_path,'Report')
print report_path
