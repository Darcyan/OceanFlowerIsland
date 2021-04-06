# coding=utf-8
from selenium_method import *
from logger import *
import time
from readConfig import get_config
from selenium.webdriver.support.select import Select


class CommonMethod(WebDriver):
    tangwu_tag = '//*[@id="banner-section"]/div/div/div[1]/div[2]/div/div/ul/li[3]/div/img[1]'  # 首页汤屋图标‘
    hotel_tag='//*[@id="banner-section"]/div/div/div[1]/div[2]/div/div/ul/li[2]/div/img[1]' #首页酒店图标‘
    ticket_tag = '//*[@id="banner-section"]/div/div/div[1]/div[2]/div/div/ul/li[1]/div/img[2]' # 首页乐园门票图标
    select_tickit_button= '// * [ @ id = "amusementForm"] / div / div[1] / div / p'  # 选择门票
    select_hotel_button= '// *[ @ id = "hotelForm"] / div / div[1] / div / p' # 选择酒店
    select_tangwu_button= '//*[@id="soupHouseForm"]/div/div[1]/div/p' # 选择汤屋
    list_li_1= '//*[@id="amusementIndex"]/li[1]'  # 下拉列表中第一个元素
    list_li_10 = '//*[@id="amusementIndex"]/li[10]' # 下拉列表中第10个元素
    logout_button = '//*[@id="logout"]' # 退出按钮
    web_url = 'https://10.101.71.11:2655/zh-cn/'
    login_button = '登录'  # 登录链接
    input_box='//*[@id="app"]/div/div[1]/div/form/div[1]/input'  # 账号输入框
    input_pwd_box = '//*[@id="app"]/div/div[1]/div/form/div[2]/input[2]' # 密码输入框
    user_login_button='//*[@id="app"]/div/ul/li[1]'   # 账户登录
    login_button2 = '//*[@id="app"]/div/div[1]/div/form/div[3]/button' # 登入按钮
    play_empty_icon='//*[@id="mainInfo"]/div[2]/div[1]/div/div[3]/div/img' # 乐园无数据图标
    hotel_empty_icon='//*[@id="app"]/div[2]/div[2]/ul/li/img' # 酒店无数据图标
    calender_icon='//*[@id="amusementDate"]/div/img' #首页日历控件
    calender_icon1 ='// *[ @ id = "hotelDate01"] / div / img'
    calender_icon2 ='// *[ @ id = "hotelDate02"] / div / img'

    def open_web(self, url=web_url):
        # 登入官网门户网站
        self.openurl(url)
        self.click_new('//*[@id="details-button"]')
        self.click_new('//*[@id="proceed-link"]')
        self.element_should_contain('xpath', '//*[@id="amusementBook"]', '预订')
        time.sleep(1)

    def booking_tickit(self, type=1):
        # 点击官网页面的预定按钮
        # 1=乐园  2=酒店  3=汤屋
        time.sleep(2)
        if type==1:
            self.click_new('//*[@id="amusementBook"]')
        elif type==2:
            self.click_new('//*[@id="hotelBook"]')
        else:
            self.click_new('//*[@id="soupHouseBook"]')

    def click_new(self, els=None):
        # 重写click
        self.click('xpath', els)

    # def select_tickit(self, xpath=select_tickit_button):
    #     # 点击下拉列表按钮
    #     self.click_new(xpath)

    def select_tickit_type(self, type=1):
        # type=1 为门票   type=2 为酒店 type=3为汤屋
        if type==1:
            self.click_new(self.select_tickit_button)
        elif type==2:
            self.click_new(self.select_hotel_button)
        else:
            self.click_new(self.select_tangwu_button)


    def select_list_value(self, xpath=list_li_10):
        # 选择列表中某一个选项，如：恒大水世界测试
        self.click_new(xpath)

    # def click_play_label(self, xpath=ticket_tag):
    #     # 点击首页的门票按钮
    #     self.click_new(xpath)

    def click_icon_type(self, type=1):
        # 点击首页门票图标 1=乐园门票，2=酒店 ， 3=汤屋
        if type==1:
            self.click_new(self.ticket_tag)
        elif type==2:
            self.click_new(self.hotel_tag)
        else:
            self.click_new(self.tangwu_tag)


    def click_hotel_tag(self, xpath=hotel_tag):
        # 点击首页的酒店按钮
        self.click_new(xpath)

    def select_down_list(self):
        nr = Select(self.driver.find_element_by_id("nr"))
        select = Select(nr) #实例化下拉框
        select.select_by_value()

    def select_play_list(self, num=0):
        # 下拉列表选择乐园
        # 先定位到下拉菜单,,num=0默认点击第一条
        ul= self.driver.find_element_by_css_selector('#amusementIndex')
        time.sleep(5)
        li= ul.find_elements_by_tag_name('li')
        # 以下方法可以解决遮罩问题
        self.driver.execute_script("arguments[0].click();", li[num])
        # 无遮罩可以使用下列方法
        # li[num].click()
        time.sleep(1)

    def select_hotel_list(self, num=0):
        # 下拉列表选择酒店
        # 先定位到下拉菜单,,num=0默认点击第一条
        ul= self.driver.find_element_by_css_selector('#hotelIndex')
        time.sleep(5)
        li= ul.find_elements_by_tag_name('li')
        # 以下方法可以解决遮罩问题
        self.driver.execute_script("arguments[0].click();", li[num])
        time.sleep(1)

    def select_tangwu_list(self, num=0):
        # 下拉列表选择汤屋
        # 先定位到下拉菜单,,num=0默认点击第一条
        ul = self.driver.find_element_by_css_selector('#soupHouseIndex')
        time.sleep(5)
        li = ul.find_elements_by_tag_name('li')
        # 以下方法可以解决遮罩问题
        self.driver.execute_script("arguments[0].click();", li[num])
        time.sleep(1)

    def enter_key(self):
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="amusementIndex"]/li[1]').send_keys(Keys.ENTER)

    def slip_scroll(self, num=1000):
        js = 'document.getElementsByClassName("select-box icon-arrow-drop").scrollTop=10000'
        # 就是这么简单，修改这个元素的scrollTop就可以
        self.driver.execute_script(js)
        time.sleep(10)

    def input_text(self, els=None, text=""):
        self.input('xpath', els, text)

    def click_by_link_text(self, text=None):
        # 点击链接
        self.driver.find_element_by_link_text(text).click()

    def clear_new(self, cle=None):
        # 重写
        self.clear('xpath', cle)

    def get_user_info(self):
        username = get_config("userinfo", "user")
        password = get_config("userinfo", "pwd")
        return username, password

    def login_user(self):
        # 登入用户名
        username, password = self.get_user_info()
        self.click_by_link_text(self.login_button)
        # self.click_new(self.user_login_button)
        self.clear_new(self.input_box)
        self.input_text(self.input_box, username)
        self.clear_new(self.input_pwd_box)
        self.input_text(self.input_pwd_box, password)
        self.click_new(self.login_button2)
        time.sleep(3)
        self.scroll_to(0, 0)
        time.sleep(2)
        self.element_should_contain('xpath', self.logout_button, '退出')
        print("退出存在")
        time.sleep(1)

    def logout_user(self):
        self.click_new(self.logout_button)
        time.sleep(1)
        self.element_should_not_contain('xpath', self.logout_button, '退出')

    def empty_icon_exist(self,type=1):
        # 检测是否当日无数据，emptyicon是否存在 1=乐园  2=为酒店或汤屋
        flag=True
        icon=self.play_empty_icon
        if type == 1:
            icon = self.play_empty_icon
        else:
            icon = self.hotel_empty_icon

        if self.element_should_contain2('xpath', icon):
            self.logger.info("当日无数据")
        else:
            self.logger.error("当日有数据")
            flag=False
        return flag

    def click_calender(self):
        # 首页酒店预订日历按钮
        self.click_new(self.calender_icon)

    def click_calendar1(self):
        # 首页酒店预订第一个日历按钮
        self.click_new(self.calender_icon1)
        time.sleep(1)

    def click_calendar2(self):
        # 首页酒店预订第二个日历按钮
        self.click_new(self.calender_icon2)
        time.sleep(1)

    def set_play_date(self, date="2021-4-24"):
        # 设置乐园预订日期
        js1 = 'document.getElementById("inAmusementDate").removeAttribute("readonly");'
        # 调用js脚本
        self.driver.execute_script(js1)
        # 通过js修改日期输入框的value值
        js2 = 'document.getElementById("inAmusementDate").value="%s";' % date
        self.driver.execute_script(js2)
        time.sleep(2)

    def set_hotel_date(self, type = 1, date="2021-4-24"):
        # type=1为开始日期，否则为结束日期，默认为1 ，设置酒店预订日期
        if type == 1:
            new_date_id = 'inHotelDate01'
        else:
            new_date_id = 'inHotelDate02'
        js1 = 'document.getElementById(new_date_id).removeAttribute("readonly");'
        # 调用js脚本
        self.driver.execute_script(js1)
        # 通过js修改日期输入框的value值
        js2 = 'document.getElementById(new_date_id).value="%s";' % date
        self.driver.execute_script(js2)
        time.sleep(2)

    def set_tangwu_date(self, type = 1, date="2021-4-24"):
        # type=1为开始日期，否则为结束日期，默认为1 ，设置汤屋预订日期
        if type == 1:
            new_date_id = 'insoupHouseDate01'
        else:
            new_date_id = 'insoupHouseDate02'
        js1 = 'document.getElementById(new_date_id).removeAttribute("readonly");'
        # 调用js脚本
        self.driver.execute_script(js1)
        # 通过js修改日期输入框的value值
        js2 = 'document.getElementById(new_date_id).value="%s";' % date
        self.driver.execute_script(js2)
        time.sleep(2)


#  -------------------------------以下为非类方法-------------------------------
def get_current_time(add_date=0):
    # add_date=0默认为当日
    today = datetime.date.today()
    current_time = today + datetime.timedelta(days=add_date)
    return current_time

