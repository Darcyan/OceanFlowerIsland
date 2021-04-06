#!/usr/bin/python
# _*_ coding: UTF-8 _*_

import logging
import os
import re
import datetime


class Logger(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level=logging.INFO)
        if 'log' not in os.listdir(os.getcwd()):
            os.mkdir('log')
        self.handler = logging.FileHandler('./log/' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".log")
        self.handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(formatter)
        self.logger.addHandler(self.handler)

    def info(self, msg):
        print('\033[36m%s' % msg)
        self.logger.info(msg)

    def error(self, msg):
        if 'img_data' in str(msg):
            # msg = str(msg) + '\n' + re.sub('raise CustomException.*', 'raise CustomException()'
            # , traceback.format_exc(), flags=re.DOTALL)
            print('\033[1;31m%s' % re.sub('(\nimg_data: .*)', '', str(msg), flags=re.DOTALL))
        else:
            print('\033[1;31m%s' % str(msg))
        self.logger.error(msg)
