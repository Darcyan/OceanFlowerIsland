# coding=utf-8
from selenium_method import *
from logger import *
import unittest
from common_method import *
from selenium import webdriver


class WebTest(unittest.TestCase):

    def setUp(self):
        print('开始执行测试用例：')
        self.logger = Logger()
        self.driver = CommonMethod(self.logger)
        self.driver.setup("chrome")

    # @unittest.skip(" tiaoshi ")
    def test_1_login(self):
        self.driver.open_web()
        self.driver.login_user()

    def test_2_logout(self):
        self.driver.open_web()
        self.driver.login_user()
        time.sleep(3)
        self.driver.logout_user()

    # @unittest.skip("no")
    def test_3_book_play_ticket(self):
        #  预定乐园门票
        self.driver.open_web()
        self.driver.click_icon_type(1)
        self.driver.select_tickit_type(1)
        self.driver.select_play_list()
        current_date= get_current_time()
        self.driver.set_play_date(current_date)
        self.driver.booking_tickit(1)
        self.driver.scroll_to(0, 800)
        time.sleep(1)
        if not self.driver.empty_icon_exist(1):
            return
        pass

    def test_4_book_hotel(self):
        # 预定酒店
        self.driver.open_web()
        self.driver.click_icon_type(2)
        self.driver.select_tickit_type(2)
        self.driver.select_hotel_list(0)
        start_time = get_current_time()
        self.driver.set_tangwu_date(date=start_time)
        end_time = get_current_time(add_date=2)
        self.driver.set_tangwu_date(type=2, date=end_time)
        self.driver.booking_tickit(2)
        self.driver.scroll_to(0, 800)
        time.sleep(1)
        if not self.driver.empty_icon_exist(2):
            return
        pass

    def test_5_book_tangwu(self):
        # 预定汤屋
        self.driver.open_web()
        self.driver.click_icon_type(3)
        self.driver.select_tickit_type(3)
        self.driver.select_tangwu_list(0)
        start_time = get_current_time()
        self.driver.set_tangwu_date(date=start_time)
        end_time = get_current_time(add_date=2)
        self.driver.set_tangwu_date(type=2, date=end_time)
        self.driver.booking_tickit(3)
        self.driver.scroll_to(0, 800)
        time.sleep(1)
        if not self.driver.empty_icon_exist(2):
            return
        pass

    def tearDown(self):
        self.driver.teardown()


if __name__ == '__main__':
    unittest.main()


