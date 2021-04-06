# coding=utf-8
# 本模块用来调试的
import ddt
import unittest
from selenium import webdriver
from common_method import *


def get_current_time(add_date=0):
    # add_date=0,默认加一天
    current_time= datetime.datetime.now().strftime('%Y-%m-%d')
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=add_date)
    return tomorrow

tomorrow=get_current_time()
tomorrow1=get_current_time(1)
tomorrow2=get_current_time(2)

print(tomorrow)
print(tomorrow1)
print(tomorrow2)
