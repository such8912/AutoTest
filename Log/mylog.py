# -*- coding: utf-8 -*-
'''
Log4j建议只使用四个级别，优先级从高到低分别是 ERROR、WARNING、INFO、DEBUG
'''
import logging
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class MyLog:

    def __init__(self, level="INFO", ):
        self.logger = logging.getLogger("自动化测试日志")
        self.logger.setLevel(logging.INFO)

        filehandler = logging.FileHandler("my.log", encoding='utf-8')
        filehandler.setLevel(logging.INFO)

        streamhandler = logging.StreamHandler()
        streamhandler.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s-%(name)s:%(levelname)s-%(message)s')

        streamhandler.setFormatter(formatter)
        filehandler.setFormatter(formatter)

        self.logger.addHandler(streamhandler)
        self.logger.addHandler(filehandler)

    def log_writing(self, level, logInfo):
        if level == "ERROR" or level == "error" or level == "Error":
            self.logger.debug(logInfo)
        elif level == "WARNING" or level == "warning" or level == "Warning":
            self.logger.warning(logInfo)
        elif level == "INFO" or level == "info" or level == "Info":
            self.logger.info(logInfo)
        elif level == "DEBUG" or level == "debug" or level == "Debug":
            self.logger.debug(logInfo)
        else:
            print u"日志级别请输入ERROR、WARNING、INFO、DEBUG"
