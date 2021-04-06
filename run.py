# coding=utf-8
from email.mime.application import MIMEApplication
from selenium_method import *
import unittest
from HTMLTestRunner import HTMLTestRunner
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from readConfig import get_config
current_path = os.getcwd()
report_path = os.path.join(current_path, "report")


def load_all_case():
    # 添加所有用例test_suite
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(current_path, pattern='*_test.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit


# 定义发送邮件
def new_report(test_report):
    lists = os.listdir(test_report)
    lists.sort(key=lambda fn:os.path.getmtime(test_report+'\\'+fn)) # 获取一个文件中的最近访问时间的文件
    file_new = os.path.join(test_report, lists[-1])
    print("==========获取最近时间生成的报告文件路径===========>"+file_new)
    return file_new


def send_mail(new_report, filename):

    sender = get_config("email", "sender")  # 读取配置文件中发件人
    sendpwd = get_config("email", "pwd")  # 读取配置文件中发件人密码
    receiver = get_config("email", "receiver")  # 读取配置文件中收件人
    smtp_server= get_config("email", "smtp_server")
    port= get_config("email", "port")

    f = open(new_report, 'rb')  # 获取报告文件
    body_main = f.read()

    # 邮件标题
    msg = MIMEMultipart()
    msg['Subject'] = Header('接口自动化测试报告', 'utf-8')
    msg['From'] = sender
    msg['To'] = receiver

    # 邮件内容
    text = MIMEText(body_main, 'html', 'utf-8')
    msg.attach(text)

    # 发送邮件
    att = MIMEApplication(open(filename, 'rb').read())
    att['Content-Type'] = 'application/octet-stream'
    att.add_header('Content-Disposition', 'attachment', filename = filename)
    msg.attach(att)

    try:
        smtp = smtplib.SMTP_SSL(host=smtp_server)
        smtp.connect(smtp_server, port)
        smtp.login(sender, sendpwd)
        smtp.sendmail(sender, receiver, msg.as_string())
        print('mail has been send successfully')
    except Exception as e:
        print(e)


if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    report_title = "OceanFlowerIsland_"+now+".html"
    result_path = os.path.join(report_path, report_title)
    desc = u"描述用例的使用"
    fp = open(result_path, 'w', encoding='utf-8')
    runner = HTMLTestRunner.HTMLTestRunner(stream = fp, title = report_title, description = desc)
    runner.run(load_all_case())
    fp.close()

    # 5、执行发送邮件
    # new_report = new_report(report_path)
    # send_mail(new_report, result_path)


