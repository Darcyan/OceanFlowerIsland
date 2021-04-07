# coding=utf-8
# 本模块用来调试的
import ddt
import unittest
from selenium import webdriver
from common_method import *
import os
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
time.sleep(2)
picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
print(picture_time)

try:
    # picture_url=driver.get_screenshot_as_file(current_direct+"_"+picture_time +'.png')
    picture_url = driver.save_screenshot('.\\' + "screenshot" + '\\' + picture_time + '.png')
    print("%s：截图成功！！！" % picture_url)
except BaseException as msg:
    print(msg)
driver.quit()