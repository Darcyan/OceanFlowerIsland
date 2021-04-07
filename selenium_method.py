#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
DesiredCapabilities.INTERNETEXPLORER['ignoreProtectedModeSettings'] = True
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pykeyboard import *
import time
import unittest
import re
import os
import json
import traceback
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from logger import *

class WebDriver(object):
    def __init__(self, logger):
        self.driver = None
        self.logger = logger
        self.locator_dict = {'css': By.CSS_SELECTOR, 'text': By.PARTIAL_LINK_TEXT, 'id': By.ID, 'name': By.NAME,
                             'class_name': By.CLASS_NAME, 'xpath': By.XPATH}

    def getdriver(self):
        driver=self.driver
        return driver

    def setup(self, browser):
        """
        网页组件初始化
        :param browser: chrome
        :return: {"result": "INFO", "msg": "web成功建立连接"}
        """
        try:
            if browser == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser == 'ie':
                DesiredCapabilities.INTERNETEXPLORER['ignoreProtectedModeSettings'] = True
                self.driver = webdriver.Ie()
            else:
                msg = '没有提供调用这种浏览器的方法'
                result = '{"result": "ERROR", "msg": "%s"}' % msg
                return result
            self.driver.maximize_window()
            msg = 'web成功建立连接'
            result = '{"result": "INFO", "msg": "%s"}' % msg
        except:
            msg = '启动浏览器错误，检查是否安装浏览器驱动'
            result = '{"result": "ERROR", "msg": "%s"}' % msg
            self.logger.error(msg)
        return result

    def openurl(self, url):
        """
        打开网页
        :param url: 'http://10.101.70.52:81'
        :return: '{"result": "INFO", "msg": "打开网址：http://10.101.70.52:81"}'
        """
        self.driver.get(url)
        msg = '打开网址：%s' % url
        result = '{"result": "INFO", "msg": "%s"}' % msg
        return result

    def current_url_should_be(self, expect_url):
        """
        判断当前url是否为预期值
        :param expect_url: 'http://10.101.70.52:81'
        :return: '{"result": "INFO", "msg": "当前url与预期相等", "flag": "True"}
        """
        if expect_url == self.driver.current_url:
            msg = '当前url与预期相等'
            flag = 'True'
            result = '{"result": "INFO", "msg": "%s", "flag": "%s"}' % (msg, flag)
        else:
            msg = '当前url与预期不相等'
            flag = 'False'
            result = '{"result": "INFO", "msg": "%s", "flag": "%s"}' % (msg, flag)
        return result

    def click(self, locator, ele, index=0, timeouts=6):
        """
        点击元素
        :param locator: 'xpath'
        :param ele: '//*[@id="index"]/div/div/div'
        :param index: 0/1/2......
        :param timeouts: 1
        :return: '{"result": "INFO", "msg": "点击 '//*[@id=\"index\"]/div/div/div' 成功"}'
        """
        try:
            if index == 0:
                WebDriverWait(self.driver, timeouts). \
                    until(EC.element_to_be_clickable((self.locator_dict[locator], ele)))
                time.sleep(0.5)
                self.driver.find_element(self.locator_dict[locator], ele).click()
            else:
                time.sleep(0.5)
                self.driver.find_elements(self.locator_dict[locator], ele)[index - 1].click()
            msg = '点击 %s 成功' % ele.replace("\"", "'")
            self.logger.info(msg)
            result = '{"result": "INFO", "msg": "%s"}' % msg
        except:
            msg = '点击 %s 失败' % ele.replace("\"", "'")
            self.logger.error(msg)
            result = '{"result": "ERROR", "msg": "%s"}' % msg
            # raise AssertionError(result)
            self.shot_screen()
            raise
        return result

    def right_click(self, locator, ele, timeouts=6):
        """
        右击元素
        :param locator: 'xpath'
        :param ele: '//*[@id="index"]/div/div/div'
        :param timeouts: 1
        :return: '{"result": "INFO", "msg": "右击 '//*[@id=\"index\"]/div/div/div' 成功"}'
        """
        try:
            WebDriverWait(self.driver, timeouts). \
                until(EC.element_to_be_clickable((self.locator_dict[locator], ele)))
            time.sleep(0.5)
            ActionChains(self.driver).context_click(self.driver.find_element(self.locator_dict[locator], ele)).perform()
            msg = '右击 %s 成功' % ele.replace("\"", "'")
            result = '{"result": "INFO", "msg": "%s"}' % msg
        except:
            msg = '右击 %s 失败' % ele.replace("\"", "'")
            self.logger.error(msg)
            result = '{"result": "ERROR", "msg": "%s"}' % msg
            # raise AssertionError(result)
        return result

    def double_click(self, locator, ele, timeouts=6):
        """
        双击元素
        :param locator: 'xpath'
        :param ele: '//*[@id="index"]/div/div/div'
        :param timeouts: 1
        :return: '{"result": "INFO", "msg": "双击 '//*[@id=\"index\"]/div/div/div' 成功"}'
        """
        try:
            WebDriverWait(self.driver, timeouts). \
                until(EC.element_to_be_clickable((self.locator_dict[locator], ele)))
            time.sleep(0.5)
            ActionChains(self.driver).double_click(self.driver.find_element(self.locator_dict[locator], ele)).perform()
            msg = '双击 %s 成功' % ele.replace("\"", "'")
            result = '{"result": "INFO", "msg": "%s"}' % msg
        except:
            msg = '双击 %s 失败' % ele.replace("\"", "'")
            self.logger.error(msg)
            result = '{"result": "ERROR", "msg": "%s"}' % msg
            # raise AssertionError(result)
        return result
     # #amusementIndex [data-orgid="b350aad675a9473cbda5313bbf778f1e"]
    def select_item(self, box_js_locator, box_ele, item_locator, item_ele, timeouts=6):
        """
        选择下拉框里的元素
        :param box_js_locator: css
        :param box_ele: 'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap'
        :param locator: 'xpath'
        :param option_ele: '//span[contains(text(), "测试开发使用")]'
        :param timeouts: 5
        :return: '{"result": "INFO", "msg": 点击 //span[contains(text(), "测试开发使用")] 成功}'
        """
        if box_js_locator == 'css':
            js = 'var q = document.querySelectorAll("%s")[0].scrollTop=' % box_ele.replace('"', '\'')
        elif box_js_locator == 'id':
            js = 'var q = document.getElementById("%s").scrollTop=' % box_ele.replace('"', '\'')
        elif box_js_locator == 'name':
            js = 'var q = document.getElementsByName("%s")[0].scrollTop=' % box_ele.replace('"', '\'')
        elif box_js_locator == 'tag':
            js = 'var q = document.getElementsByTagName("%s")[0].scrollTop=' % box_ele.replace('"', '\'')
        elif box_js_locator == 'class':
            js = 'var q = document.getElementsByClassName("%s")[0].scrollTop=' % box_ele.replace('"', '\'')
        else:
            msg = '无 %s 这一定位器' % box_js_locator
            return '{"result": "ERROR", "msg": "%s"}' % msg
        temp_height = 0
        temp_start_time = int(time.time())
        temp_end_time = int(time.time())
        time.sleep(0.5)
        while temp_end_time - temp_start_time < timeouts:
            try:
                temp_ele = self.driver.find_element(item_locator, item_ele)
                # 增加偏移量，令点击更准确
                # if temp_ele.size.values() != [0, 0]:
                ActionChains(self.driver).move_to_element(temp_ele).move_by_offset(temp_ele.size['width'] / 2.5,
                                                                                   temp_ele.size[
                                                                                       'height'] / 2.5).click().perform()
                msg = '点击 %s 成功' % item_ele.replace("\"", "'")
                return '{"result": "INFO", "msg": "%s"}' % msg
            except:
                temp_js = js + str(temp_height)
                self.execute_script(temp_js)
                temp_height += 10
            temp_end_time = int(time.time())
        msg = '点击 %s 失败' % item_ele.replace("\"", "'")
        raise AssertionError(msg)
        #  return '{"result": "ERROR", "msg": "%s"}' % msg

    def drag_and_drop(self, source_locator, target_locator, source_ele, target_ele, timeouts=6):
        """
        拖动元素
        :param source_locator: 'xpath'
        :param target_locator: 'xpath'
        :param source_ele: '//*[@id="app"]/div/div/form/div[2]/div/div[1]/input'
        :param target_ele: '//*[@id="app"]/div/div/form/div[3]/div/div/input'
        :param timeouts: 1
        :return: '{"result": "ERROR", "msg": "拖动 //*[@id=\"app\"]/div/div/form/div[2]/div/div[1]/input 至 //*[@id=\"app\"]/div/div/form/div[3]/div/div/input 成功"}'
        """
        try:
            WebDriverWait(self.driver, timeouts). \
                until(EC.element_to_be_clickable((self.locator_dict[source_locator], source_ele)))
            time.sleep(0.5)
            ActionChains(self.driver).drag_and_drop(
                self.driver.find_element(self.locator_dict[source_locator], source_ele),
                self.driver.find_element(self.locator_dict[target_locator], target_ele)).perform()
            msg = '拖动 %s 至 %s 成功' % (source_ele.replace("\"", "'"), target_ele.replace("\"", "'"))
            result = '{"result": "INFO", "msg": "%s"}' % msg
        except:
            msg = '拖动 %s 至 %s 失败' % (source_ele.replace("\"", "'"), target_ele.replace("\"", "'"))
            self.logger.error(msg)
            result = '{"result": "ERROR", "msg": "%s"}' % msg
        return result

    def clear(self, locator, ele, index=0, timeouts=6):
        """
        清空元素
        :param locator: 'xpath'
        :param ele: '//*[@id="app"]/div/div/form/div[2]/div/div[1]/input'
        :param index: 0/1/2......
        :param timeouts: 1
        :return: '{"result": "INFO", "msg": "清空 //*[@id=\"app\"]/div/div/form/div[2]/div/div[1]/input 成功"}'
        """
        try:
            if index == 0:
                WebDriverWait(self.driver, timeouts). \
                    until(EC.element_to_be_clickable((self.locator_dict[locator], ele)))
                for i in range(1, 100):
                    temp_ele = self.driver.find_element(self.locator_dict[locator], ele)
                    temp_ele.send_keys(Keys.BACK_SPACE)
                    if temp_ele.get_attribute('value') == '':
                        break
            else:
                for i in range(1, 100):
                    temp_ele = self.driver.find_elements(self.locator_dict[locator], ele)[index - 1]
                    temp_ele.send_keys(Keys.BACK_SPACE)
                    if temp_ele.get_attribute('value') == '':
                        break
            # self.driver.find_element(self.locator_dict[locator], ele).clear()
            msg = '清空 %s 成功' % ele.replace("\"", "'")
            result = '{"result": "INFO", "msg": "%s"}' % msg
        except:
            msg = '清空 %s 失败' % ele.replace("\"", "'")
            self.logger.error(msg)
            result = '{"result": "ERROR", "msg": "%s"}' % msg
        return result

    def input(self, locator, ele, text, index=0, timeouts=6):
        """
        向元素信息输入
        :param locator: 'xpath'
        :param ele: '//*[@id="app"]/div/div/form/div[2]/div/div[1]/input'
        :param text: 'test'
        :param index: 0/1/2......
        :param timeouts: 1
        :return: '{"result": "INFO", "msg": "输入：test"}'
        """
        try:
            if index == 0:
                WebDriverWait(self.driver, timeouts). \
                    until(EC.element_to_be_clickable((self.locator_dict[locator], ele)))
                self.driver.find_element(self.locator_dict[locator], ele).send_keys(text)
            else:
                time.sleep(0.5)
                self.driver.find_elements(self.locator_dict[locator], ele)[index - 1].send_keys(text.decode('utf8'))
            msg = '输入：%s' % text
            self.logger.info(msg)
            result = '{"result": "INFO", "msg": "%s"}' % msg
        except:
            msg = '输入 %s 失败' % text
            self.logger.error(msg)
            result = '{"result": "ERROR", "msg": "%s"}' % msg
        return result

    def element_should_be_enabled(self, locator, ele, timeouts=6):
        """
        验证元素是可用的
        :param locator: 'xpath'
        :param ele: '//*[@id="app"]/div/div/form/div[2]/div/div[1]/input'
        :param timeouts: 1
        :return: '{"result": "INFO", "msg": "元素 //*[@id="app"]/div/div/form/div[2]/div/div[1]/input 可用", "flag": "True"}'
        """
        try:
            WebDriverWait(self.driver, timeouts).until(EC.element_to_be_clickable((self.locator_dict[locator], ele)))
            msg = '元素 %s 可用' % ele.replace("\"", "'")
            flag = 'True'
            result = '{"result": "INFO", "msg": "%s", "flag": "%s"}' % (msg, flag)
        except:
            msg = '元素 %s 不可用' % ele.replace("\"", "'")
            self.logger.error(msg)
            flag = 'False'
            result = '{"result": "INFO", "msg": "%s", "flag": "%s"}' % (msg, flag)
        return result

    def element_should_not_be_enabled(self, locator, ele, timeouts=6):
        """
        验证元素是不可用的
        :param locator: 'xpath'
        :param ele: '//*[@id="app"]/div/div/form/div[2]/div/div[1]/input'
        :param timeouts: 1
        :return: '{"result": "INFO", "msg": "元素 //*[@id="app"]/div/div/form/div[2]/div/div[1]/input 不可用", "flag": "True"}'
        """
        try:
            WebDriverWait(self.driver, timeouts).until_not(
                EC.element_to_be_clickable((self.locator_dict[locator], ele)))
            msg = '元素 %s 不可用' % ele.replace("\"", "'")
            flag = 'True'
            result = '{"result": "INFO", "msg": "%s", "flag": "%s"}' % (msg, flag)
        except:
            msg = '元素 %s 可用' % ele.replace("\"", "'")
            self.logger.error(msg)
            flag = 'False'
            result = '{"result": "INFO", "msg": "%s", "flag": "%s"}' % (msg, flag)
        return result

    def element_should_be_visible(self, locator, ele, timeouts=6):
        """
        验证元素是可见的
        :param locator: 'xpath'
        :param ele: '//*[@id="app"]/div/div/form/div[2]/div/div[1]/input'
        :param timeouts: 1
        :return: '{"result": "INFO", "msg": "元素 //*[@id="app"]/div/div/form/div[2]/div/div[1]/input 可见", "flag": "True"}'
        """
        try:
            WebDriverWait(self.driver, timeouts).until(
                EC.visibility_of_element_located((self.locator_dict[locator], ele)))
            msg = '元素 %s 可见' % ele.replace("\"", "'")
            flag = 'True'
            result = '{"result": "INFO", "msg": "%s", "flag": "%s"}' % (msg, flag)
        except:
            msg = '元素 %s 不可见' % ele.replace("\"", "'")
            self.logger.error(msg)
            flag = 'False'
            result = '{"result": "INFO", "msg": "%s", "flag": "%s"}' % (msg, flag)
        return result

    def element_should_not_be_visible(self, locator, ele, timeouts=6):
        """
        验证元素是不可见的
        :param locator: 'xpath'
        :param ele: '//*[@id="app"]/div/div/form/div[2]/div/div[1]/input'
        :param timeouts: 1
        :return: '{"result": "INFO", "msg": "元素 //*[@id="app"]/div/div/form/div[2]/div/div[1]/input 不可见", "flag": "True"}'
        """
        try:
            WebDriverWait(self.driver, timeouts).until_not(
                EC.visibility_of_element_located((self.locator_dict[locator], ele)))
            msg = '元素 %s 不可见' % ele.replace("\"", "'")
            flag = 'True'
            result = '{"result": "INFO", "msg": "%s", "flag": "%s"}' % (msg, flag)
        except:
            msg = '元素 %s 可见' % ele.replace("\"", "'")
            self.logger.error(msg)
            flag = 'False'
            result = '{"result": "INFO", "msg": "%s", "flag": "%s"}' % (msg, flag)
        return result

    def element_should_contain(self, locator, ele, expext_text, timeouts=6):
        """
        验证元素文本包含预期文本
        :param locator: 'xpath'
        :param ele: '//*[@id="app"]/div/div/form/div[2]/div/div[1]/input'
        :param expext_text: text
        :param timeouts: 1
        :return: '{"result": "INFO", "msg": "文本 'text' 在元素 //*[@id="app"]/div/div/form/div[2]/div/div[1]/input 中", "flag": "True"}'
        """
        try:
            WebDriverWait(self.driver, timeouts).until(
                EC.visibility_of_element_located((self.locator_dict[locator], ele)))
            # 元素的标签
            label = re.findall('/([\w\d]*)', ele)[-1]
            if label == 'textarea' or label == 'input':
                text = self.driver.find_element(self.locator_dict[locator], ele).get_attribute('value')
            else:
                text = self.driver.find_element(self.locator_dict[locator], ele).text
            if expext_text in text:
                msg = '文本 \'%s\' 在元素 %s 中' % (expext_text, ele.replace("\"", "'"))
                flag = 'True'
                result = '{"result": "INFO", "msg": "%s", "flag": "%s"}' % (msg, flag)
            else:
                msg = '文本 \'%s\' 不在元素 %s 中' % (expext_text, ele.replace("\"", "'"))
                flag = 'False'
                result = '{"result": "ERROR", "msg": "%s", "flag": "%s"}' % (msg, flag)
        except:
            msg = '元素 %s 不可见' % ele.replace("\"", "'")
            self.logger.error(msg)
            result = '{"result": "ERROR", "msg": "%s"}' % msg
            self.capture_screen()
            raise
        return result

    def element_should_contain2(self, locator, ele, timeouts=6):
        """
        验证元素文本包含预期文本
        :param locator: 'xpath'
        :param ele: '//*[@id="app"]/div/div/form/div[2]/div/div[1]/input'
        :param timeouts: 1
        :return: '{"result": "INFO", "msg": "文本 'text' 在元素 //*[@id="app"]/div/div/form/div[2]/div/div[1]/input 中", "flag": "True"}'
        """
        try:
            WebDriverWait(self.driver, timeouts).until(
                EC.visibility_of_element_located((self.locator_dict[locator], ele)))
            # 元素的标签
            label = re.findall('/([\w\d]*)', ele)[-1]

        except:
            msg = '元素 %s 不可见' % ele.replace("\"", "'")
            self.logger.error(msg)
            result = '{"result": "ERROR", "msg": "%s"}' % msg
            self.logger.info(result)
            self.shot_screen()
            return False

        return True

    def element_should_not_contain(self, locator, ele, expext_text, timeouts=6):
        """
        验证元素文本不包含预期文本
        :param locator: 'xpath'
        :param ele: '//*[@id="app"]/div/div/form/div[2]/div/div[1]/input'
        :param expext_text: text
        :param timeouts: 1
        :return: '{"result": "INFO", "msg": "文本 'text' 不在元素 //*[@id="app"]/div/div/form/div[2]/div/div[1]/input 中", "flag": "True"}'
        """
        try:
            WebDriverWait(self.driver, timeouts).until(
                EC.visibility_of_element_located((self.locator_dict[locator], ele)))
            # 元素的标签
            label = re.findall('/([\w\d]*)', ele)[-1]
            if label == 'textarea' or label == 'input':
                text = self.driver.find_element(self.locator_dict[locator], ele).get_attribute('value')
            else:
                text = self.driver.find_element(self.locator_dict[locator], ele).text
            if expext_text in text:
                msg = '文本 \'%s\' 在元素 %s 中' % (expext_text, ele.replace("\"", "'"))
                flag = 'False'
                result = '{"result": "INFO", "msg": "%s", "flag": "%s"}' % (msg, flag)

            else:
                msg = '文本 \'%s\' 不在元素 %s 中' % (expext_text, ele.replace("\"", "'"))
                flag = 'True'
                result = '{"result": "ERROR", "msg": "%s", "flag": "%s"}' % (msg, flag)
            logger.error(result)
            raise
        except:
            msg = '元素 %s 不可见' % ele.replace("\"", "'")
            self.logger.info(msg)
            result = '{"result": "ERROR", "msg": "%s"}' % msg
            return True

        return result

    def element_text_should_be(self, locator, ele, expext_text, timeouts=6):
        """
        验证元素文本等于预期文本
        :param locator: 'xpath'
        :param ele: '//*[@id="app"]/div/div/form/div[2]/div/div[1]/input'
        :param expext_text: text
        :param timeouts: 1
        :return: '{"result": "INFO", "msg": "文本 'text' 等于元素 //*[@id="app"]/div/div/form/div[2]/div/div[1]/input 文本", "flag": "True"}'
        """
        try:
            WebDriverWait(self.driver, timeouts).until(
                EC.visibility_of_element_located((self.locator_dict[locator], ele)))
            # 元素的标签
            label = re.findall('/([\w\d]*)', ele)[-1]
            if label == 'textarea' or label == 'input':
                text = self.driver.find_element(self.locator_dict[locator], ele).get_attribute('value')
            else:
                text = self.driver.find_element(self.locator_dict[locator], ele).text
            if expext_text == text:
                msg = '文本 \'%s\' 等于元素 %s 文本: %s' % (expext_text, ele.replace("\"", "'"), text)
                flag = 'True'
                result = '{"result": "INFO", "msg": "%s", "flag": "%s"}' % (msg, flag)
            else:
                msg = '文本 \'%s\' 不等于元素 %s 文本: %s' % (expext_text, ele.replace("\"", "'"), text)
                flag = 'False'
                result = '{"result": "ERROR", "msg": "%s", "flag": "%s"}' % (msg, flag)
        except:
            msg = '元素 %s 不可见' % ele.replace("\"", "'")
            self.logger.error(msg)
            result = '{"result": "ERROR", "msg": "%s"}' % msg
            raise AssertionError(result)
        return result

    def element_should_be_selected(self, locator, ele, timeouts=6):
        """
        验证元素是被选中的
        :param locator: 'xpath'
        :param ele: '//*[@id="app"]/div/div/form/div[2]/div/div[1]/input'
        :param timeouts: 1
        :return: '{"result": "INFO", "msg": "元素 //*[@id="app"]/div/div/form/div[2]/div/div[1]/input 被选中", "flag": "True"}'
        """
        try:
            WebDriverWait(self.driver, timeouts).until(
                EC.element_located_to_be_selected((self.locator_dict[locator], ele)))
            is_selected = self.driver.find_element(self.locator_dict[locator], ele).is_selected()
            if is_selected is True:
                msg = '元素 %s 被选中' % ele.replace("\"", "'")
                flag = 'True'
            else:
                msg = '元素 %s 未被选中' % ele.replace("\"", "'")
                flag = 'False'
            result = '{"result": "INFO", "msg": "%s", "flag": "%s"}' % (msg, flag)
        except:
            msg = '元素 %s 不可选' % ele.replace("\"", "'")
            self.logger.error(msg)
            result = '{"result": "ERROR", "msg": "%s"}' % msg
            raise AssertionError(result)
        return result

    def element_should_not_be_selected(self, locator, ele, timeouts=6):
        """
        验证元素是未被选中的
        :param locator: 'xpath'
        :param ele: '//*[@id="app"]/div/div/form/div[2]/div/div[1]/input'
        :param timeouts: 1
        :return: '{"result": "INFO", "msg": "元素 //*[@id="app"]/div/div/form/div[2]/div/div[1]/input 被选中", "flag": "True"}'
        """
        try:
            WebDriverWait(self.driver, timeouts).until(
                EC.element_located_to_be_selected((self.locator_dict[locator], ele)))
            is_selected = self.driver.find_element(self.locator_dict[locator], ele).is_selected()
            if is_selected is False:
                msg = '元素 %s 未被选中' % ele.replace("\"", "'")
                flag = 'True'
            else:
                msg = '元素 %s 被选中' % ele.replace("\"", "'")
                flag = 'False'
            result = '{"result": "INFO", "msg": "%s", "flag": "%s"}' % (msg, flag)
        except:
            msg = '元素 %s 不可选' % ele.replace("\"", "'")
            self.logger.error(msg)
            result = '{"result": "ERROR", "msg": "%s"}' % msg
            raise AssertionError(result)
        return result

    def get_page_source(self):
        """
        获取网页源代码
        :return: '{"result": "INFO", "msg": "%s"，"page_source": "网页源码"}'
        """
        try:
            page_sources = self.driver.page_source
            msg = '获取网页源码成功'
            result = '{"result": "INFO", "msg": "%s"，"page_source": "%s"}' % (msg, page_sources.replace("\"", "'"))
        except:
            msg = '获取网页源码失败'
            result = '{"result": "ERROR", "msg": "%s"}' % msg
            raise AssertionError(result)
        return result

    def get_element_text(self, locator, ele, timeouts=6):
        """
        获取元素文本
        :param locator: 'xpath'
        :param ele: '//*[@id="app"]/div/div/form/div[2]/div/div[1]/input'
        :param index: 0/1/2......
        :param timeouts: 1
        :return: '{"result": "INFO", "msg": "test"}'
        """
        try:
            WebDriverWait(self.driver, timeouts). \
                until(EC.visibility_of_element_located((self.locator_dict[locator], ele)))
            # 元素的标签
            label = re.findall(r'/([\w\d]*)', ele)[-1]
            if label == 'textarea' or label == 'input':
                msg = self.driver.find_element(self.locator_dict[locator], ele).get_attribute('value')
            else:
                msg = self.driver.find_element(self.locator_dict[locator], ele).text
            result = {"result": "INFO", "msg": msg}
            # self.logger.info(result)
        except:
            msg = '获取文本失败'
            self.logger.error(msg)
            raise AssertionError(msg)
        return msg

    def get_element_attr(self, locator, ele, attr, index=0, timeouts=6):
        """
        获取元素属性
        :param locator: 'xpath'
        :param ele: '//*[@id="app"]/div/div/form/div[2]/div/div[1]/input'
        :param attr: class
        :param index: 0/1/2......
        :param timeouts: 1
        :return: '{"result": "INFO", "msg": "test"}'
        """
        try:
            if index == 0:
                WebDriverWait(self.driver, timeouts). \
                    until(EC.element_to_be_clickable((self.locator_dict[locator], ele)))
                time.sleep(0.5)
                msg = self.driver.find_element(self.locator_dict[locator], ele).get_attribute(attr)
            else:
                time.sleep(0.5)
                msg = self.driver.find_elements(self.locator_dict[locator], ele)[index - 1].get_attribute(attr)
            result = '{"result": "INFO", "msg": "%s"}' % msg.replace("\"", "'")
            return result
        except:
            msg = '获取元素失败'
            self.logger.error(msg)
            result = '{"result": "INFO", "msg": "%s"}' % msg
            raise AssertionError(result)
        return result

    def switch_to_window(self, index):
        """
        切换窗口
        :param index: 0
        :return: '{"result": "INFO", "msg": "切换到第1个窗口"}'
        """
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[index])
        msg = '切换到第%d个窗口' % (index + 1)
        result = '{"result": "INFO", "msg": "%s"}' % msg
        return result

    def close_current_window(self):
        """
        关闭当前窗口
        :return: '{"result": "INFO", "msg": "关闭当前窗口"}'
        """
        self.driver.close()
        msg = '关闭当前窗口'
        result = '{"result": "INFO", "msg": "%s"}' % msg
        return result

    def refresh(self):
        """
        刷新页面
        :return: '{"result": "INFO", "msg": "刷新页面"}'
        """
        self.driver.refresh()
        msg = '刷新页面'
        result = '{"result": "INFO", "msg": "%s"}' % msg
        return result

    def capture_screen(self):
        """
        截图
        :return: '{"result": "INFO", "msg": "截图成功", "img": "图片编码"}'
        """
        try:
            img_data = str(self.driver.get_screenshot_as_base64())
            msg = '截图成功'
            result = '{"result": "INFO", "msg": "%s", "img": "%s"}' % (msg, img_data)
        except:
            msg = '截图失败'
            self.logger.error(msg)
            result = '{"result": "ERROR", "msg": "%s"}' % msg
            raise AssertionError(result)
        return result

    def shot_screen(self):
        time.sleep(2)
        picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        try:
            picture_url = self.driver.save_screenshot('.\\' + "screenshot" + '\\' + picture_time + '.png')
            print("%s：截图成功！！！" % picture_url)
        except BaseException as msg:
            print(msg)
            raise
        self.quit()
        return

    def upload_file(self, locator, ele, file_path):
        """
                上传文件，需要定位上传文件的input元素
                :param locator: 'xpath'
                :param ele: '//*[@id="app"]/section/section/main/div/div/div[9]/div/div[2]/div/div[1]/input'
                :param file_path: 'F:\test.xml'
                :param timeouts: 1
                :return: '{"result": "INFO", "msg": "%上传文件 test.xml 成功"}'
                """
        try:
            # WebDriverWait(self.driver, timeouts). \
            #     until(EC.element_to_be_clickable((self.locator_dict[locator], ele)))
            time.sleep(0.5)
            self.driver.find_element(self.locator_dict[locator], ele).send_keys(file_path.decode('utf8'))
            msg = '上传文件 %s 成功' % os.path.basename(file_path)
            result = '{"result": "INFO", "msg": "%s"}' % msg
        except:
            print(traceback.format_exc())
            msg = '上传文件 %s 失败' % os.path.basename(file_path)
            self.logger.error(msg)
            result = '{"result": "ERROR", "msg": "%s"}' % msg
            raise AssertionError(result)
        return result

    def handle_alert(self, handle=0):
        """
        处理弹框
        :param handle: 处理方式，0为接受，1为拒绝
        :param timeouts: 超时
        :return: {"result": "INFO", "msg": "%s"}
        """
        # end_time = start_time = int(time.time())
        # while end_time - start_time < timeouts:

        try:
            if handle == 0:
                alert = self.driver.switch_to.alert
                alert.accept()
                # keyboard = PyKeyboard()
                # keyboard.press_key(keyboard.alt_key)
                # keyboard.tap_key(keyboard.tab_key)
                # time.sleep(0.5)
                # keyboard.release_key(keyboard.alt_key)
                # # keyboard.tap_key(keyboard.tab_key)
                # # keyboard.tap_key(keyboard.enter_key)
                # time.sleep(1)
                # keyboard.tap_key('y')
            else:
                # self.driver.switch_to_alert().dismiss()
                # self.driver.switch_to_alert().send_keys(Keys.ENTER)
                keyboard = PyKeyboard()
                keyboard.press_key(keyboard.alt_key)
                keyboard.tap_key(keyboard.tab_key)
                keyboard.release_key(keyboard.alt_key)
                time.sleep(1)
                keyboard.tap_key('n')
            msg = '处理弹框成功'
            return '{"result": "INFO", "msg": "%s"}' % msg
        except:
            # end_time = int(time.time())
            # continue
            msg = '处理弹框失败'
            self.logger.error(msg)
            raise AssertionError(msg)
        return True

    def execute_script(self, js):
        """
        执行js脚本
        :param js: var q = document.getElementsByClassName("el-scrollbar__wrap")[0].scrollTop=10000
        :return: '{"result": "INFO", "msg": "执行js var q = document.getElementsByClassName("el-scrollbar__wrap")[0].scrollTop=10000 指令成功"}'
        """
        try:
            self.driver.execute_script(js)
            msg = '执行js指令成功'
            result = '{"result": "INFO", "msg": "%s"}' % msg
        except:
            msg = '执行js指令失败'
            self.logger.error(msg)
            result = '{"result": "ERROR", "msg": "%s"}' % msg
            raise AssertionError(result)
        return result

    def scroll_to(self, x, y):
        """
        滚动页面至某处
        :param x: 0
        :param y: 10000
        :return: '{"result": "INFO", "msg": "滚动至(0, 10000)"}'
        """
        self.execute_script('window.scrollTo(%d, %d)' % (x, y))
        msg = '滚动至(%d, %d)' % (x, y)
        return '{"result": "INFO", "msg": "%s"}' % msg

    def teardown(self):
        """
        关闭网页组件
        :return: '{"result": "INFO", "msg": "web断开连接"}'
        """
        if self.driver is not None:
            self.driver.quit()
            self.driver = None
        msg = 'web断开连接'
        result = '{"result": "INFO", "msg": "%s"}' % msg
        return result

    def input_keys(self, locator, ele):
        """
        输入按键
        :param locator: 'xpath'
        :param ele: '//*[@id="app"]/section/section/main/div/div/div[9]/div/div[2]/div/div[1]/input'
        :param key: "Keys.ENTER / (Keys.CONTROL,'a')"
        :return: '{"result": "INFO", "msg": "键入按键Enter成功"}'
        """
        self.driver.find_element(self.locator_dict[locator], ele).send_keys(Keys.ENTER)
        msg = '键入Enter成功'
        result = '{"result": "INFO", "msg": "%s"}' % msg
        return result

    def input_tab_enter(self):
        """
        输入按键
        :param locator: 'xpath'
        :param ele: '//*[@id="app"]/section/section/main/div/div/div[9]/div/div[2]/div/div[1]/input'
        :param key: "Keys.ENTER / (Keys.CONTROL,'a')"
        :return: '{"result": "INFO", "msg": "键入按键Enter成功"}'
        """
        keyboard = PyKeyboard()
        keyboard.tap_key(keyboard.tab_key)
        keyboard.tap_key(keyboard.enter_key)
        msg = '键入Enter成功'
        result = '{"result": "INFO", "msg": "%s"}' % msg
        return result

    def set_session_storage(self, key, value):
        try:
            if isinstance(value, str):
                self.execute_script("sessionStorage.setItem('%s', '%s')" % (key, value))
            else:
                self.execute_script("sessionStorage.setItem('%s', '%s')" % (key, json.dumps(value).replace("'", '"')))
            msg = 'sessionStorage保存成功'
            result = '{"result": "INFO", "msg": "%s"}' % msg
        except:
            print(traceback.format_exc())
            msg = 'sessionStorage保存失败'
            result = '{"result": "ERROR", "msg": "%s"}' % msg
            raise AssertionError(result)
        return result

    def set_local_storage(self, key, value):
        try:
            if isinstance(value, str):
                self.execute_script("localStorage.setItem('%s', '%s')" % (key, value))
            else:
                self.execute_script("localStorage.setItem('%s', '%s')" % (key, json.dumps(value).replace("'", '"')))
            msg = 'localStorage保存成功'
            result = '{"result": "INFO", "msg": "%s"}' % msg
        except:
            print(traceback.format_exc())
            msg = 'localStorage保存失败'
            result = '{"result": "ERROR", "msg": "%s"}' % msg
        return result

    def get_screen_size(self):
        # 获取浏览器屏幕尺寸
        size_dict = self.driver.get_window_size()
        x = size_dict['width']
        y = size_dict['height']
        return x, y


if __name__ == '__main__':
    logger = Logger()
    web = WebDriver(logger)
    web.setup('chrome')
    web.openurl('https://www.baidu.com/')

   # #  time.sleep(10)
   # # web.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')

    # print("----11----")
    # print(web.openurl('http://10.101.70.52:81'))
    # print(web.input('xpath', '//*[@id="app"]/div/div/form/div[2]/div/div[1]/input', 'test', 0, 6))
    # print(web.input('xpath', '//*[@id="app"]/div/div/form/div[3]/div/div/input', 'test', 0, 6))
    # print(web.element_should_be_enabled('xpath', '//*[@id="index"]/div/div/div', 180))
    # time.sleep(3)
    # print(web.execute_script('var q = document.getElementsByTagName("a")[11].click()'))
    # time.sleep(1)
    # print(web.execute_script('var q = document.querySelectorAll(".el-menu-item")[8].click()'))
    # time.sleep(3)
    # web.handle_alert(0)
    # time.sleep(1)
    # web.handle_alert(0)
    # time.sleep(1)
    # web.handle_alert(0)
    # print(web.element_should_be_enabled('xpath', '//article[@class="device-img"]/div/p/img', 6))
    # time.sleep(10)
    # time.sleep(3)
    # print(web.teardown())

