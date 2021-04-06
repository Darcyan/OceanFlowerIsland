# coding=utf-8
from selenium_method import *
from logger import *
import time


def web_get_charging_rules_func(driver, parajson, logger):
    """
    done
    :param driver:
    :param parajson:
    :return:
    """
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('css', ".is-opened .el-menu-item:nth-child(1)")
    driver.input('xpath', "//input[@id='ruleName']", paradic['rules_name'])
    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/div[1]/form/div[5]/div/button[1]/span')
    time.sleep(2)

    get_name = driver.get_element_text('xpath',
                                       "//div[contains(@class,'el-table__body-wrapper is-scrolling-none')]//td[3]//div[1]")
    logger.info('查询到的名称是：{}'.format(get_name))
    print('查询到的名称是：{}'.format(get_name))
    if get_name == paradic['rules_name']:
        res = {'code': 0, 'message': 'GET SUCCESS 查询成功'}
        logger.info(res)
        print(res)
        return res
    else:
        res = {'code': 1, 'message': 'GET FAIL 查询失败'}
        logger.info(res)
        print(res)
        return res


def web_update_charging_rules_by_count_func(driver, parajson, logger):
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('css', ".is-opened .el-menu-item:nth-child(1)")
    driver.input('xpath', "//input[@id='ruleName']", paradic['rules_name'])
    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/div[1]/form/div[5]/div/button[1]/span')
    # parajson = json.dumps(parajson)
    # paradic = json.loads(parajson)
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    # driver.click('css', ".is-opened .el-menu-item:nth-child(1)")
    #
    # driver.input('xpath', "//input[@id='ruleName']", paradic['rules_name'])
    # driver.click('xpath', "//form[@class='el-form el-form--inline']//span")
    # driver.click('xpath', "//div[contains(@class,'el-table__fixed-right')]//button[1]//span[1]")  # 编辑
    #
    # driver.clear('xpath', "//div[@class='memo-text']//input")
    # driver.input('xpath', "//div[@class='memo-text']//input", paradic['rules_name'])
    #
    # driver.clear('xpath', "//div[@class='memo-text']//textarea")
    # driver.input('xpath', "//div[@class='memo-text']//textarea", paradic['rules_desc'])
    #
    # # 小车免费时间
    # driver.clear('xpath', "//div[@id='editFeeId']//tr[1]//td[2]//input[1]")
    # driver.input('xpath', "//div[@id='editFeeId']//tr[1]//td[2]//input[1]",
    #              paradic['small_car_free_time'])
    #
    # driver.clear('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[1]/td[3]/input')
    # driver.input('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[1]/td[3]/input',
    #              paradic['small_car_charge'])
    #
    # driver.clear('xpath', "//div[@id='editFeeId']//tr[2]//td[2]//input[1]")
    # driver.input('xpath', "//div[@id='editFeeId']//tr[2]//td[2]//input[1]",
    #              paradic['big_car_free_time'])
    #
    # driver.clear('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[2]/td[3]/input')
    # driver.input('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[2]/td[3]/input',
    #              paradic['big_car_charge'])
    #
    # driver.clear('xpath', "//div[@id='editFeeId']//tr[3]//td[2]//input[1]")
    # driver.input('xpath', "//div[@id='editFeeId']//tr[3]//td[2]//input[1]",
    #              paradic['superbig_car_free_time'])
    #
    # driver.clear('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[3]/td[3]/input')
    # driver.input('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[3]/td[3]/input',
    #              paradic['superbig_car_charge'])
    #
    # driver.clear('xpath', "//div[@id='editFeeId']//tr[4]//td[2]//input[1]")
    # driver.input('xpath', "//div[@id='editFeeId']//tr[4]//td[2]//input[1]",
    #              paradic['moto_car_free_time'])
    #
    # driver.clear('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[4]/td[3]/input')
    # driver.input('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[4]/td[3]/input',
    #              paradic['moto_car_charge'])
    #
    # driver.click('xpath', "//div[@id='editFeeId']//div//input[@placeholder='请选择车型']")
    # time.sleep(1)
    # driver.click('xpath', "/html[1]/body[1]/div[3]/div[1]/div[1]/ul[1]/li[2]")
    # time.sleep(1)
    # driver.input('xpath', "//div[@class='el-dialog__body']//div[2]//div[1]//div[1]//input[1]",
    #              paradic['car_in_time'])
    # driver.click('xpath', "//div[@id='editFeeId']")
    #
    # driver.input('xpath',
    #              "//div[@class='el-form-item is-required']//input[@class='el-input__inner']",
    #              paradic['car_out_time'])
    # driver.click('xpath', "//div[@id='editFeeId']")
    #
    # time.sleep(1)
    # driver.click('xpath',
    #              "//form[@class='el-form']//button[@class='el-button el-button--primary']//span")  # 计算
    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/div[2]/div[4]/div[2]/table/tbody/tr[1]/td[7]/div/button[1]/span')

    driver.input('xpath', '//input[@placeholder="请选择入场时间"]', paradic['car_in_time'])
    driver.input('xpath', '//input[@placeholder="请选择出场时间"]', paradic['car_out_time'])
    time.sleep(1)
    driver.click('xpath', '//*[@id="editFeeId"]/section[2]/button[2]/span')  # 保存
    time.sleep(2)
    res = {'code': 0, 'message': 'UPDATE SUCCESS 更新成功'}
    logger.info(res)
    print(res)
    return res


def web_update_charging_rules_by_time_func(driver, parajson, logger):
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('css', ".is-opened .el-menu-item:nth-child(1)")
    driver.input('xpath', "//input[@id='ruleName']", paradic['rules_name'])
    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/div[1]/form/div[5]/div/button[1]/span')

    # driver.input('xpath', "//input[@id='ruleName']",
    #              paradic['rules_name'])
    # driver.click('xpath', "//form[@class='el-form el-form--inline']//span")
    # driver.click('xpath', "//div[contains(@class,'el-table__fixed-right')]//button[1]//span[1]")  # 编辑
    #
    # driver.clear('xpath', "//div[@class='memo-text']//input")
    # driver.input('xpath', "//div[@class='memo-text']//input",
    #              paradic['rules_name'])
    #
    # driver.clear('xpath', "//div[@class='memo-text']//textarea")
    # driver.input('xpath', "//div[@class='memo-text']//textarea", paradic['rules_desc'])
    #
    # # 小车免费时间
    # driver.clear('xpath', "//div[@id='editFeeId']//tr[1]//td[2]//input[1]")
    # driver.input('xpath', "//div[@id='editFeeId']//tr[1]//td[2]//input[1]",
    #              paradic['small_car_free_time'])
    #
    # driver.clear('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[1]/td[3]/input')
    # driver.input('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[1]/td[3]/input',
    #              paradic['small_car_charge'])
    #
    # driver.clear('xpath', "//div[@id='editFeeId']//tr[2]//td[2]//input[1]")
    # driver.input('xpath', "//div[@id='editFeeId']//tr[2]//td[2]//input[1]",
    #              paradic['big_car_free_time'])
    #
    # driver.clear('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[2]/td[3]/input')
    # driver.input('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[2]/td[3]/input',
    #              paradic['big_car_charge'])
    #
    # driver.clear('xpath', "//div[@id='editFeeId']//tr[3]//td[2]//input[1]")
    # driver.input('xpath', "//div[@id='editFeeId']//tr[3]//td[2]//input[1]",
    #              paradic['superbig_car_free_time'])
    #
    # driver.clear('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[3]/td[3]/input')
    # driver.input('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[3]/td[3]/input',
    #              paradic['superbig_car_charge'])
    #
    # driver.clear('xpath', "//div[@id='editFeeId']//tr[4]//td[2]//input[1]")
    # driver.input('xpath', "//div[@id='editFeeId']//tr[4]//td[2]//input[1]",
    #              paradic['moto_car_free_time'])
    #
    # driver.clear('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[4]/td[3]/input')
    # driver.input('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[4]/td[3]/input',
    #              paradic['moto_car_charge'])
    #
    # driver.click('xpath', "//div[@id='editFeeId']//div//input[@placeholder='请选择车型']")
    # time.sleep(1)
    # driver.click('xpath', "/html[1]/body[1]/div[3]/div[1]/div[1]/ul[1]/li[2]")
    # time.sleep(1)
    # driver.input('xpath', "//div[@class='el-dialog__body']//div[2]//div[1]//div[1]//input[1]",
    #              paradic['car_in_time'])
    # driver.click('xpath', "//div[@id='editFeeId']")
    #
    # driver.input('xpath',
    #              "//div[@class='el-form-item is-required']//input[@class='el-input__inner']",
    #              paradic['car_out_time'])
    # driver.click('xpath', "//div[@id='editFeeId']")
    #
    # time.sleep(1)
    # driver.click('xpath',
    #              "//form[@class='el-form']//button[@class='el-button el-button--primary']//span")  # 计算
    # time.sleep(1)
    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/div[2]/div[4]/div[2]/table/tbody/tr[1]/td[7]/div/button[1]/span')

    driver.input('xpath', '//input[@placeholder="请选择入场时间"]', paradic['car_in_time'])
    driver.input('xpath', '//input[@placeholder="请选择出场时间"]', paradic['car_out_time'])
    time.sleep(1)
    driver.click('xpath', '//*[@id="editFeeId"]/section[2]/button[2]/span')  # 保存
    res = {'code': 0, 'message': 'UPDATE SUCCESS 更新成功'}
    logger.info(res)
    print(res)
    return res


def web_update_charging_rules_by_stage_func(driver, parajson, logger):
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('css', ".is-opened .el-menu-item:nth-child(1)")
    driver.input('xpath', "//input[@id='ruleName']", paradic['rules_name'])
    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/div[1]/form/div[5]/div/button[1]/span')

    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/div[2]/div[4]/div[2]/table/tbody/tr[1]/td[7]/div/button[1]/span')  # 编辑

    # driver.clear('xpath', "//div[@class='memo-text']//input")
    # driver.input('xpath', "//div[@class='memo-text']//input",
    #              paradic['rules_name'])
    #
    # driver.clear('xpath', "//div[@class='memo-text']//textarea")
    # driver.input('xpath', "//div[@class='memo-text']//textarea", paradic['rules_desc'])
    #
    # # 小车免费时间
    # driver.clear('xpath', "//div[@id='editFeeId']//tr[1]//td[2]//input[1]")
    # driver.input('xpath', "//div[@id='editFeeId']//tr[1]//td[2]//input[1]",
    #              paradic['small_car_free_time'])
    #
    # driver.clear('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[1]/td[3]/input')
    # driver.input('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[1]/td[3]/input',
    #              paradic['small_car_charge'])
    #
    # driver.clear('xpath', "//div[@id='editFeeId']//tr[2]//td[2]//input[1]")
    # driver.input('xpath', "//div[@id='editFeeId']//tr[2]//td[2]//input[1]",
    #              paradic['big_car_free_time'])
    #
    # driver.clear('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[2]/td[3]/input')
    # driver.input('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[2]/td[3]/input',
    #              paradic['big_car_charge'])
    #
    # driver.clear('xpath', "//div[@id='editFeeId']//tr[3]//td[2]//input[1]")
    # driver.input('xpath', "//div[@id='editFeeId']//tr[3]//td[2]//input[1]",
    #              paradic['superbig_car_free_time'])
    #
    # driver.clear('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[3]/td[3]/input')
    # driver.input('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[3]/td[3]/input',
    #              paradic['superbig_car_charge'])
    #
    # driver.clear('xpath', "//div[@id='editFeeId']//tr[4]//td[2]//input[1]")
    # driver.input('xpath', "//div[@id='editFeeId']//tr[4]//td[2]//input[1]",
    #              paradic['moto_car_free_time'])
    #
    # driver.clear('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[4]/td[3]/input')
    # driver.input('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[4]/td[3]/input',
    #              paradic['moto_car_charge'])
    #
    # driver.click('xpath', "//div[@id='editFeeId']//div//input[@placeholder='请选择车型']")
    # time.sleep(1)
    # driver.click('xpath', "/html[1]/body[1]/div[3]/div[1]/div[1]/ul[1]/li[2]")
    # time.sleep(1)
    # driver.input('xpath', "//div[@class='el-dialog__body']//div[2]//div[1]//div[1]//input[1]",
    #              paradic['car_in_time'])
    # driver.click('xpath', "//div[@id='editFeeId']").click()
    #
    # driver.input('xpath',
    #              "//div[@class='el-form-item is-required']//input[@class='el-input__inner']",
    #              paradic['car_out_time'])
    # driver.click('xpath', "//div[@id='editFeeId']")
    #
    # time.sleep(1)
    # driver.click('xpath',
    #              "//form[@class='el-form']//button[@class='el-button el-button--primary']//span")  # 计算
    driver.input('xpath', '//input[@placeholder="请选择入场时间"]', paradic['car_in_time'])
    driver.input('xpath', '//input[@placeholder="请选择出场时间"]', paradic['car_out_time'])
    time.sleep(1)
    driver.click('xpath', '//*[@id="editFeeId"]/section[2]/button[2]/span')  # 保存
    res = {'code': 0, 'message': 'UPDATE SUCCESS 更新成功'}
    logger.info(res)
    print(res)
    return res


def web_update_charging_rules_by_period_func(driver, parajson, logger):
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('css', ".is-opened .el-menu-item:nth-child(1)")
    driver.input('xpath', "//input[@id='ruleName']", paradic['rules_name'])
    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/div[1]/form/div[5]/div/button[1]/span')

    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/div[2]/div[4]/div[2]/table/tbody/tr[1]/td[7]/div/button[1]/span')  # 编辑

    # driver.clear('xpath', "//div[@class='memo-text']//input")
    # driver.input('xpath', "//div[@class='memo-text']//input",
    #              paradic['rules_name'])
    #
    # driver.clear('xpath', "//div[@class='memo-text']//textarea")
    # driver.input('xpath', "//div[@class='memo-text']//textarea", paradic['rules_desc'])
    #
    # # 小车免费时间
    # driver.clear('xpath', "//div[@id='editFeeId']//tr[1]//td[2]//input[1]")
    # driver.input('xpath', "//div[@id='editFeeId']//tr[1]//td[2]//input[1]",
    #              paradic['small_car_free_time'])
    #
    # driver.clear('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[1]/td[3]/input')
    # driver.input('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[1]/td[3]/input',
    #              paradic['small_car_charge'])
    #
    # driver.clear('xpath', "//div[@id='editFeeId']//tr[2]//td[2]//input[1]")
    # driver.input('xpath', "//div[@id='editFeeId']//tr[2]//td[2]//input[1]",
    #              paradic['big_car_free_time'])
    #
    # driver.clear('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[2]/td[3]/input')
    # driver.input('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[2]/td[3]/input',
    #              paradic['big_car_charge'])
    #
    # driver.clear('xpath', "//div[@id='editFeeId']//tr[3]//td[2]//input[1]")
    # driver.input('xpath', "//div[@id='editFeeId']//tr[3]//td[2]//input[1]",
    #              paradic['superbig_car_free_time'])
    #
    # driver.clear('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[3]/td[3]/input')
    # driver.input('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[3]/td[3]/input',
    #              paradic['superbig_car_charge'])
    #
    # driver.clear('xpath', "//div[@id='editFeeId']//tr[4]//td[2]//input[1]")
    # driver.input('xpath', "//div[@id='editFeeId']//tr[4]//td[2]//input[1]",
    #              paradic['moto_car_free_time'])
    #
    # driver.clear('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[4]/td[3]/input')
    # driver.input('xpath', '//*[@id="editFeeId"]/section[1]/form/table/tbody/tr[4]/td[3]/input',
    #              paradic['moto_car_charge'])
    #
    # driver.click('xpath', "//div[@id='editFeeId']//div//input[@placeholder='请选择车型']")
    # time.sleep(1)
    # driver.click('xpath', "/html[1]/body[1]/div[3]/div[1]/div[1]/ul[1]/li[2]")
    # time.sleep(1)
    # driver.input('xpath', "//div[@class='el-dialog__body']//div[2]//div[1]//div[1]//input[1]",
    #              paradic['car_in_time'])
    # driver.click('xpath', "//div[@id='editFeeId']")
    #
    # driver.input('xpath',
    #              "//div[@class='el-form-item is-required']//input[@class='el-input__inner']",
    #              paradic['car_out_time'])
    # driver.click('xpath', "//div[@id='editFeeId']")
    #
    # time.sleep(1)
    # driver.click('xpath',
    #              "//form[@class='el-form']//button[@class='el-button el-button--primary']//span")  # 计算
    driver.input('xpath', '//input[@placeholder="请选择入场时间"]', paradic['car_in_time'])
    driver.input('xpath', '//input[@placeholder="请选择出场时间"]', paradic['car_out_time'])
    time.sleep(1)
    driver.click('xpath', '//*[@id="editFeeId"]/section[2]/button[2]/span')  # 保存
    res = {'code': 0, 'message': 'UPDATE SUCCESS 更新成功'}
    logger.info(res)
    print(res)
    return res


def web_delete_charging_rules_func(driver, parajson, logger):
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('css', ".is-opened .el-menu-item:nth-child(1)")
    driver.input('xpath', "//input[@id='ruleName']", paradic['rules_name'])
    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/div[1]/form/div[5]/div/button[1]/span')
    time.sleep(2)
    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/div[2]/div[4]/div[2]/table/tbody/tr[1]/td[7]/div/button[3]/span')
    driver.click('xpath', '/html/body/div[2]/div/div[3]/button[2]/span')
    time.sleep(2)
    res = {'code': 0, 'message': 'DELETE SUCCESS 删除成功'}
    print(res)
    logger.info(res)
    return res


def web_add_charging_rules_by_count_func(driver, parajson, logger):
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('css', ".is-opened .el-menu-item:nth-child(1)")
    driver.click('css', ".fee-btns > .el-button--primary > span")  # 添加
    driver.click('css', ".mt15 .el-input__inner")
    driver.click('id', "addFee")
    driver.input('css', ".is-required:nth-child(1) .el-input__inner",
                 paradic['rules_name'])
    driver.input('css', ".el-textarea__inner", paradic['rules_desc'])

    driver.click('css', "table:nth-child(3) > tbody > tr:nth-child(1)")
    driver.clear('css', "tr:nth-child(1) > td:nth-child(2) > input")
    driver.input('css', "tr:nth-child(1) > td:nth-child(2) > input",
                 paradic['small_car_free_time'])

    driver.click('css', "table:nth-child(3) > tbody > tr:nth-child(1)")
    driver.clear('css', "tr:nth-child(1) > td:nth-child(3) > input")
    driver.input('css', "tr:nth-child(1) > td:nth-child(3) > input",
                 paradic['small_car_charge'])

    driver.click('css', "table:nth-child(3) tr:nth-child(2)")
    driver.clear('css', "tr:nth-child(2) > td:nth-child(2) > input")
    driver.input('css', "tr:nth-child(2) > td:nth-child(2) > input",
                 paradic['big_car_free_time'])

    driver.click('css', "table:nth-child(3) tr:nth-child(2)")
    driver.clear('css', "tr:nth-child(2) > td:nth-child(3) > input")
    driver.input('css', "tr:nth-child(2) > td:nth-child(3) > input",
                 paradic['big_car_charge'])

    driver.click('css', "table:nth-child(3) tr:nth-child(3)")
    driver.clear('css', "tr:nth-child(3) > td:nth-child(2) > input")
    driver.input('css', "tr:nth-child(3) > td:nth-child(2) > input",
                 paradic['superbig_car_free_time'])

    driver.click('css', "table:nth-child(3) tr:nth-child(3)")
    driver.clear('css', "tr:nth-child(3) > td:nth-child(3) > input")
    driver.input('css', "tr:nth-child(3) > td:nth-child(3) > input",
                 paradic['superbig_car_charge'])

    driver.click('css', "table:nth-child(3) tr:nth-child(4)")
    driver.clear('css', "tr:nth-child(4) > td:nth-child(2) > input")
    driver.input('css', "tr:nth-child(4) > td:nth-child(2) > input",
                 paradic['moto_car_free_time'])

    driver.click('css', "table:nth-child(3) tr:nth-child(4)")
    driver.clear('css', "tr:nth-child(4) > td:nth-child(3) > input")
    driver.input('css', "tr:nth-child(4) > td:nth-child(3) > input",
                 paradic['moto_car_charge'])

    driver.click('css', ".el-form-item__content > .el-select .el-input__inner")
    time.sleep(1)
    driver.click('xpath', "/html[1]/body[1]/div[4]/div[1]/div[1]/ul[1]/li[1]")
    time.sleep(1)
    driver.input('xpath', '//*[@id="addFeeTimeId"]/form/div[2]/form/div[2]/div/div/input',
                 paradic['car_in_time'])

    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[3]/div/div[1]')

    driver.input('xpath', '//*[@id="addFeeTimeId"]/form/div[2]/form/div[3]/div/div/input',
                 paradic['car_out_time'])
    time.sleep(1)
    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[3]/div/div[1]')
    time.sleep(1)

    driver.click('xpath', "//div[@class='el-dialog__wrapper']//button[2]")
    time.sleep(2)
    res = {'code': 0, 'message': 'ADD SUCCESS 添加成功'}
    logger.info(res)
    print(res)
    return res


def web_add_charging_rules_by_time_func(driver, parajson, logger):
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[1]')
    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/section/button[1]/span')  # 添加
    driver.click('xpath', "//div[@class='el-input el-input--suffix']//input[@placeholder='请选择']")
    driver.click('xpath', '/html/body/div[3]/div[1]/div[1]/ul/li[2]/span')
    driver.input('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/div[1]/div/div[1]/input',
                 paradic['rules_name'])
    driver.input('xpath', "//textarea[@class='el-textarea__inner']", paradic['rules_desc'])

    if paradic['rules_name'] == '大车':
        driver.click('xpath', '//*[@id="tab-大车"]')
        # 大车
        driver.clear('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/table/tbody/tr[1]/td[1]/input')
        driver.input('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/table/tbody/tr[1]/td[1]/input',
                     paradic['big_car_free_time'])
        driver.click('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/table/tbody/tr[1]/td[1]/label/span[1]/span')

        driver.clear('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/table/tbody/tr[1]/td[2]/input')
        driver.input('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/table/tbody/tr[1]/td[2]/input',
                     paradic['big_car_charge'])
        driver.click('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/table/tbody/tr[1]/td[2]/label/span[1]/span')

    elif paradic['rules_name'] == '超大车':
        driver.click('xpath', '//*[@id="tab-超大车"]')
        driver.clear('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/table/tbody/tr[1]/td[1]/input')
        driver.input('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/table/tbody/tr[1]/td[1]/input',
                     paradic['superbig_car_free_time'])
        driver.click('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/table/tbody/tr[1]/td[1]/label/span[1]/span')

        driver.clear('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/table/tbody/tr[1]/td[2]/input')
        driver.input('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/table/tbody/tr[1]/td[2]/input',
                     paradic['superbig_car_charge'])
        driver.click('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/table/tbody/tr[1]/td[2]/label/span[1]/span')

    elif paradic['rules_name'] == '摩托车':
        driver.click('xpath', '//*[@id="tab-摩托车"]')
        driver.clear('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/table/tbody/tr[1]/td[1]/input')
        driver.input('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/table/tbody/tr[1]/td[1]/input',
                     paradic['moto_car_free_time'])
        driver.click('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/table/tbody/tr[1]/td[1]/label/span[1]/span')

        driver.clear('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/table/tbody/tr[1]/td[2]/input')
        driver.input('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/table/tbody/tr[1]/td[2]/input',
                     paradic['moto_car_charge'])
        driver.click('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/table/tbody/tr[1]/td[2]/label/span[1]/span')

    else:
        driver.clear('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/div[4]/table/tbody[1]/tr/td[1]/input')
        driver.input('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/div[4]/table/tbody[1]/tr/td[1]/input',
                     paradic['small_car_free_time'])
        driver.click('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/div[4]/table/tbody[1]/tr/td[1]/label/span[1]/span')
        driver.clear('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/div[4]/table/tbody[1]/tr/td[2]/input')
        driver.input('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/div[4]/table/tbody[1]/tr/td[2]/input',
                     paradic['small_car_highest_charge'])
        driver.click('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/div[4]/table/tbody[1]/tr/td[2]/label/span[1]/span')

    # 时间段
    # driver.clear('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/div[4]/article/div/table/tbody[1]/tr[1]/td[2]/div[1]/input')
    # driver.input('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/div[4]/article/div/table/tbody[1]/tr[1]/td[2]/div[1]/input',
    #              paradic['time_start'])
    # driver.clear('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/div[4]/article/div/table/tbody[1]/tr[1]/td[2]/div[2]/input')
    # driver.input('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/div[4]/article/div/table/tbody[1]/tr[1]/td[2]/div[2]/input',
    #              paradic['time_end'])
    #
    # driver.clear('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/div[4]/article/div/table/tbody[1]/tr[1]/td[3]/input[1]')
    # driver.input('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/div[4]/article/div/table/tbody[1]/tr[1]/td[3]/input[1]',
    #              paradic['high_charge_several_minutes'])
    # driver.clear('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/div[4]/article/div/table/tbody[1]/tr[1]/td[3]/input[2]')
    # driver.input('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/div[4]/article/div/table/tbody[1]/tr[1]/td[3]/input[2]',
    #              paradic['high_several_minutes'])
    # 非高峰期价格
    # driver.clear('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/article/div/table/tbody[3]/tr[2]/td[3]/input[1]')
    # driver.input('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/article/div/table/tbody[3]/tr[2]/td[3]/input[1]',
    #              paradic['charge_several_minutes'])
    # driver.clear('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/article/div/table/tbody[3]/tr[2]/td[3]/input[2]')
    # driver.input('xpath', '//*[@id="addFeeIntervalId"]/form/div[1]/article/div/table/tbody[3]/tr[2]/td[3]/input[2]',
    #              paradic['several_minutes'])
    driver.input('xpath', '//input[@placeholder="请选择入场时间"]', paradic['car_in_time'])
    driver.input('xpath', '//input[@placeholder="请选择出场时间"]', paradic['car_out_time'])
    # 保存
    driver.click('xpath', '//*[@id="addFeeIntervalId"]/form/div[3]/div/button[2]/span')
    driver.click('xpath', '//*[@id="addFeeIntervalId"]/form/div[3]/div/button[2]/span')
    time.sleep(2)
    res = {'code': 0, 'message': 'ADD SUCCESS 添加成功'}
    logger.info(res)
    print(res)
    return res


def web_add_charging_rules_by_stage_func(driver, parajson, logger):
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[1]')
    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/section/button[1]/span')  # 添加
    driver.click('xpath', "//div[@class='el-input el-input--suffix']//input[@placeholder='请选择']")
    driver.click('xpath', '/html/body/div[3]/div[1]/div[1]/ul/li[3]/span')

    driver.input('xpath', '//*[@id="addFeeLadder"]/form/div[1]/div[1]/div/div/input',
                 paradic['rule_name'])
    driver.input('xpath', '//*[@id="addFeeLadder"]/form/div[1]/div[2]/div/div/textarea',
                 paradic['rules_desc'])

    if paradic['rules_name'] == '大车':
        driver.click('xpath', '//*[@id="tab-大车"]')
        # 大车
        driver.clear('xpath', '//*[@id="addFeeLadder"]/form/div[1]/div[5]/table/tbody/tr/td[2]/input')
        driver.input('xpath', '//*[@id="addFeeLadder"]/form/div[1]/div[5]/table/tbody/tr/td[2]/input',
                     paradic['big_car']['period'][0]['money'])

    elif paradic['rules_name'] == '超大车':
        driver.click('xpath', '//*[@id="tab-超大车"]')
        driver.clear('xpath', '//*[@id="addFeeLadder"]/form/div[1]/div[6]/table/tbody/tr/td[2]/input')
        driver.input('xpath', '//*[@id="addFeeLadder"]/form/div[1]/div[6]/table/tbody/tr/td[2]/input',
                     paradic['superbig_car']['period'][0]['money'])

    elif paradic['rules_name'] == '摩托车':
        driver.click('xpath', '//*[@id="tab-摩托车"]')
        driver.clear('xpath', '//*[@id="addFeeLadder"]/form/div[1]/div[7]/table/tbody/tr/td[2]/input')
        driver.input('xpath', '//*[@id="addFeeLadder"]/form/div[1]/div[7]/table/tbody/tr/td[2]/input',
                     paradic['moto_car']['period'][0]['money'])

    else:
        driver.clear('xpath', '//*[@id="addFeeLadder"]/form/div[1]/div[4]/table/tbody/tr/td[2]/input')
        driver.input('xpath', '//*[@id="addFeeLadder"]/form/div[1]/div[4]/table/tbody/tr/td[2]/input',
                     paradic['small_car']['period'][0]['money'])

    driver.input('xpath', '//input[@placeholder="请选择入场时间"]', paradic['car_in_time'])
    driver.input('xpath', '//input[@placeholder="请选择出场时间"]', paradic['car_out_time'])
    time.sleep(2)

    driver.click('xpath', '//*[@id="addFeeLadder"]/form/div[3]/div/button[2]/span')

    res = {'code': 0, 'message': 'ADD SUCCESS 添加成功'}
    logger.info(res)
    print(res)
    return res


def web_add_charging_rules_by_period_func(driver, parajson, logger):
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[1]')
    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/section/button[1]/span')  # 添加
    driver.click('xpath', "//div[@class='el-input el-input--suffix']//input[@placeholder='请选择']")
    driver.click('xpath', '/html/body/div[3]/div[1]/div[1]/ul/li[4]/span')

    driver.input('xpath', '//*[@id="addFeePhaseId"]/div[1]/div[1]/div/div/input', paradic['rules_name'])
    driver.input('xpath', '//*[@id="addFeePhaseId"]/div[1]/div[2]/div/div/textarea',
                 paradic['rules_desc'])


    driver.input('xpath', '//input[@placeholder="请选择入场时间"]', paradic['car_in_time'])
    driver.input('xpath', '//input[@placeholder="请选择出场时间"]', paradic['car_out_time'])
    time.sleep(2)
    driver.click('xpath', '//*[@id="addFeePhaseId"]/div[3]/div/button[2]/span')
    driver.click('xpath', '//*[@id="addFeePhaseId"]/div[3]/div/button[2]/span')

    res = {'code': 0, 'message': 'ADD SUCCESS 添加成功'}
    logger.info(res)
    print(res)
    return res


def web_get_resv_car_func(driver, parajson, logger):
    """
    done
    :param driver:
    :param parajson:
    :return:
    """
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath',"//body//div[@id='app']//div//div//li[1]//div[1]")
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[3]')
    driver.click('xpath',"//li[1]//ul[1]//li[3]")

    # driver.click('xpath', "//input[@placeholder='请选择预约方式']")
    # driver.click('xpath', '/html/body/div[2]/div[1]/div[1]/ul/li[1]/span')
    #
    # driver.click('xpath', "//input[@placeholder='请选择预约类型']")
    # driver.click('xpath', '/html/body/div[3]/div[1]/div[1]/ul/li[2]/span')
    #
    # driver.click('xpath', "//input[@placeholder='请选择预约业态']")
    #
    # driver.click('xpath', "//input[@placeholder='请选择部门']")

    driver.input('xpath', "//input[@placeholder='请输入车牌号码']", paradic['car_no'])
    # driver.click('xpath',"//body/div[@id='app']/section/section/main/div/div/form/div/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")

    # driver.input('xpath', "//input[@placeholder='请输入联系人']", paradic['con_name'])
    # driver.input('xpath', "//input[@placeholder='请输入联系方式']", paradic['con_method'])
    # driver.input('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/form/div[3]/div[2]/div/div/div/input[1]',
    #              paradic['begin_data'])
    # driver.input('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/form/div[3]/div[2]/div/div/div/input[2]',
    #              paradic['end_data'])
    # 查询
    driver.click('xpath', "//div[@class='search-box']//button[1]//span[1]")

    res = {'code': 0, 'message': 'GET SUCCESS 查询成功'}
    logger.info(res)
    print(res)
    return res


def web_add_resv_car_func(driver, parajson, logger):
    """
    done
    :param driver:
    :param parajson:
    :return:
    """
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # time.sleep(200)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[3]')
    # 添加
    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[2]/button[1]/span')
    # time.sleep(1000)
    driver.click('xpath',
                 '//*[@id="app"]/section/section/main/div[3]/div[5]/div/div[2]/div/form/div[1]/div[3]/div/div/div/input')
    driver.click('xpath', '/html[1]/body[1]/div[3]/div[1]/div/div[2]/div[1]/div[1]/span[2]')

    driver.click('xpath', "//input[contains(@placeholder,'请选择车场')]")
    driver.click('xpath', '/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/div[5]/div[1]/span[2]')

    driver.input('xpath', '//*[@id="app"]/section/section/main/div[3]/div[5]/div/div[2]/div/form/div[1]/div[5]/div/div/div/input',
                 paradic['car_no'])

    driver.input('xpath',
                 '//*[@id="app"]/section/section/main/div[3]/div[5]/div/div[2]/div/form/div[1]/div[6]/div/div/div/input',
                 paradic['con_name'])

    driver.input('xpath',
                 '//*[@id="app"]/section/section/main/div[3]/div[5]/div/div[2]/div/form/div[1]/div[7]/div/div/div/input',
                 paradic['con_method'])

    driver.click('xpath', "//input[contains(@placeholder,'请选择车型')]")
    driver.click('xpath', '/html/body/div[5]/div[1]/div[1]/ul/li[1]/span')

    driver.click('xpath', "//input[contains(@placeholder,'请选择车辆动力类型')]")
    driver.click('xpath', '/html/body/div[6]/div[1]/div[1]/ul/li[1]/span')

    # driver.click('xpath',
    #              '//*[@id="app"]/section/section/main/div[3]/div[5]/div/div[2]/div/form/div[1]/div[10]/div/div/div/input[1]')
    # driver.clear('xpath', '/html/body/div[8]/div[1]/div/div[1]/span[1]/span[1]/div/input')
    # driver.input('xpath', '/html/body/div[8]/div[1]/div/div[1]/span[1]/span[1]/div/input',
    #              paradic['begin_data'][:10])
    # driver.clear('xpath', '/html/body/div[8]/div[1]/div/div[1]/span[1]/span[2]/div[1]/input')
    # driver.input('xpath', '/html/body/div[8]/div[1]/div/div[1]/span[1]/span[2]/div[1]/input',
    #              paradic['begin_data'][11:])
    # driver.clear('xpath', '/html/body/div[8]/div[1]/div/div[1]/span[3]/span[1]/div/input')
    # driver.input('xpath', '/html/body/div[8]/div[1]/div/div[1]/span[3]/span[1]/div/input',
    #              paradic['end_data'][:10])
    # driver.clear('xpath', '/html/body/div[8]/div[1]/div/div[1]/span[3]/span[2]/div[1]/input')
    # driver.input('xpath', '/html/body/div[8]/div[1]/div/div[1]/span[3]/span[2]/div[1]/input',
    #              paradic['end_data'][11:])
    # driver.click('xpath', '/html/body/div[8]/div[2]/button[2]/span')
    #
    # driver.input('xpath',
    #              '//*[@id="app"]/section/section/main/div[3]/div[5]/div/div[2]/div/form/div[2]/div/div/div/textarea',
    #              '说明')

    # 保存
    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[5]/div/div[2]/div/form/div[3]/button/span')

    res = {'code': 0, 'message': 'ADD SUCCESS 添加成功'}
    logger.info(res)
    print(res)
    return res


def web_update_resv_car_func(driver, parajson, logger):
    """
    done
    :param driver:
    :param parajson:
    :return:
    """
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # time.sleep(200)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[3]')

    driver.input('xpath', "//div[@class='el-form-item']//input[@placeholder='请输入车牌号码']",
                 paradic['car_no'])
    # 查询
    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/form/div[4]/div/button[1]/span')

    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[3]/div[3]/table/tbody/tr/td[13]/div/button[2]/span')
    #
    # driver.click('xpath',
    #              '//*[@id="app"]/section/section/main/div[3]/div[5]/div/div[2]/div/form/div[1]/div[3]/div/div/div/input')
    # driver.click('xpath', '//*[@id="el-popover-5283"]/div[1]/div/div[2]/div[1]/div[1]/span[2]')

    driver.clear('xpath',
                 '//*[@id="app"]/section/section/main/div[3]/div[5]/div/div[2]/div/form/div[1]/div[6]/div/div/div/input')
    driver.input('xpath',
                 '//*[@id="app"]/section/section/main/div[3]/div[5]/div/div[2]/div/form/div[1]/div[6]/div/div/div/input',
                 paradic['con_name'])
    #
    # driver.clear('xpath',
    #              '//*[@id="app"]/section/section/main/div[3]/div[5]/div/div[2]/div/form/div[1]/div[7]/div/div/div/input')
    # driver.input('xpath',
    #              '//*[@id="app"]/section/section/main/div[3]/div[5]/div/div[2]/div/form/div[1]/div[7]/div/div/div/input',
    #              paradic['con_method'])
    #
    # driver.click('xpath',
    #              '//*[@id="app"]/section/section/main/div[3]/div[5]/div/div[2]/div/form/div[1]/div[8]/div/div/div/div[1]/input')
    # driver.click('xpath', '/html/body/div[4]/div[1]/div[1]/ul/li[1]/span')

    # driver.click('xpath',
    #              '//*[@id="app"]/section/section/main/div[3]/div[5]/div/div[2]/div/form/div[1]/div[9]/div/div/div/div[1]/input')
    # driver.click('xpath', '/html/body/div[5]/div[1]/div[1]/ul/li[1]/span')
    #
    # driver.click('xpath',
    #              '//*[@id="app"]/section/section/main/div[3]/div[5]/div/div[2]/div/form/div[1]/div[10]/div/div/div/input[1]')
    # driver.clear('xpath', '/html/body/div[6]/div[1]/div/div[1]/span[1]/span[1]/div/input')
    # driver.input('xpath', '/html/body/div[6]/div[1]/div/div[1]/span[1]/span[1]/div/input',
    #              paradic['begin_data'][:10])
    # driver.clear('xpath', '/html/body/div[6]/div[1]/div/div[1]/span[1]/span[2]/div[1]/input')
    # driver.input('xpath', '/html/body/div[6]/div[1]/div/div[1]/span[1]/span[2]/div[1]/input',
    #              paradic['begin_data'][11:])
    # driver.clear('xpath', '/html/body/div[6]/div[1]/div/div[1]/span[3]/span[1]/div/input')
    # driver.input('xpath', '/html/body/div[6]/div[1]/div/div[1]/span[3]/span[1]/div/input',
    #              paradic['end_data'][:10])
    # driver.clear('xpath', '/html/body/div[6]/div[1]/div/div[1]/span[3]/span[2]/div[1]/input')
    # driver.input('xpath', '/html/body/div[6]/div[1]/div/div[1]/span[3]/span[2]/div[1]/input',
    #              paradic['end_data'][11:])
    # driver.click('xpath', '/html/body/div[6]/div[2]/button[2]/span')

    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[5]/div/div[2]/div/form/div[3]/button/span')

    res = {'code': 0, 'message': 'UPDATE SUCCESS 更新成功'}
    logger.info(res)
    print(res)
    return res


def web_delete_resv_car_func(driver, parajson, logger):
    """
        done
        :param driver:
        :param parajson:
        :return:
    """
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # time.sleep(200)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[3]')

    driver.input('xpath', "//div[@class='el-form-item']//input[@placeholder='请输入车牌号码']",
                 paradic['car_no'])
    # 查询
    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/form/div[4]/div/button[1]/span')

    driver.click('xpath',
                 '//*[@id="app"]/section/section/main/div[3]/div[3]/div[3]/table/tbody/tr[1]/td[13]/div/button[3]/span')
    driver.click('xpath', '/html/body/div[2]/div/div[3]/button[2]/span')

    res = {'code': 0, 'message': 'DELETE SUCCESS 删除成功'}
    logger.info(res)
    print(res)
    return res


def web_get_black_list_func(driver, parajson, logger):
    """
    done
    :param driver:
    :param parajson:
    :return:
    """
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # time.sleep(200)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[4]')

    driver.input('xpath', "//input[contains(@placeholder,'请输入车牌号码')]", paradic['car_no'])

    # driver.click('xpath', "//input[contains(@placeholder,'请选择黑名单类型')]")
    # driver.click('xpath', '/html/body/div[3]/div[1]/div[1]/ul/li[2]/span')
    #
    # driver.click('xpath', "//input[contains(@placeholder,'请选择状态')]")
    # driver.click('xpath', '/html/body/div[4]/div[1]/div[1]/ul/li[1]/span')
    #
    # driver.input('xpath', "//input[contains(@placeholder,'请输入联系人')]", paradic['car_no'])
    #
    # driver.input('xpath', "//input[contains(@placeholder,'请输入联系方式')]", paradic['car_no'])
    #
    # driver.input('xpath', "//input[contains(@placeholder,'请输入操作人')]", 'xiao')
    # 查询
    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/form/div[3]/div/button[1]/span')

    res = {'code': 0, 'message': 'GET SUCCESS 查询成功'}
    logger.info(res)
    print(res)
    return res


def web_add_black_list_func(driver, parajson, logger):
    """
    done
    :param driver:
    :param parajson:
    :return:
    """
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # time.sleep(200)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[4]')
    # 添加
    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[2]/div/button[1]/span')

    driver.input('xpath',
                 '//*[@id="app"]/section/section/main/div[3]/div[5]/div/div[2]/div/div/div/form/div[1]/div[1]/div/div/div/input',
                 paradic['car_no'])

    driver.click('xpath',
                 '//*[@id="app"]/section/section/main/div[3]/div[5]/div/div[2]/div/div/div/form/div[1]/div[2]/div/div/div/div[1]/input')
    driver.click('xpath', '/html/body/div[3]/div[1]/div[1]/ul/li/span[text()="{}"]'.format(paradic['list_type']))

    driver.click('xpath', "//input[@placeholder='请选择车型']")
    driver.click('xpath', '/html/body/div[4]/div[1]/div[1]/ul/li/span[text()="{}"]'.format(paradic['car_type']))

    driver.click('xpath', "//input[contains(@placeholder,'请选择车辆动力类型')]")
    driver.click('xpath', '/html/body/div[5]/div[1]/div[1]/ul/li[1]/span[text()="{}"]'.format(paradic['move_type']))

    driver.click('xpath', "//input[contains(@placeholder,'请选择车辆所有人')]")
    driver.click('xpath', '/html/body/div[6]/div[1]/div[1]/ul/li/span[text()="{}"]'.format(paradic['car_own_type']))

    driver.input('xpath',
                 '//*[@id="app"]/section/section/main/div[3]/div[5]/div/div[2]/div/div/div/form/div[2]/div[3]/div/div/div/input',
                 paradic['con_name'])

    driver.input('xpath',
                 '//*[@id="app"]/section/section/main/div[3]/div[5]/div/div[2]/div/div/div/form/div[3]/div[1]/div/div/div/input',
                 paradic['con_method'])

    # driver.click('xpath', "//input[contains(@placeholder,'开始时间')]")
    # driver.click('xpath', '/html/body/div[10]/div[1]/div/div[1]/table/tbody/tr[3]/td[4]/div/span')
    # driver.click('xpath', '/html/body/div[10]/div[1]/div/div[2]/table/tbody/tr[5]/td[7]/div/span')

    # 保存
    driver.click('xpath',
                 '//*[@id="app"]/section/section/main/div[3]/div[5]/div/div[2]/div/div/div/form/div[5]/button/span')

    res = {'code': 0, 'message': 'ADD SUCCESS 添加成功'}
    logger.info(res)
    print(res)
    return res


def web_update_black_list_func(driver, parajson, logger):
    """
    done
    :param driver:
    :param parajson:
    :return:
    """
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # time.sleep(200)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[4]')

    driver.input('xpath', "//input[@placeholder='请输入车牌号码']", paradic['car_no'])
    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/form/div[3]/div/button[1]/span')

    # 编辑
    driver.click('xpath',
                 '//*[@id="app"]/section/section/main/div[3]/div[3]/div[3]/table/tbody/tr/td[12]/div/button[2]/span')

    # driver.click('xpath',
    #              '//*[@id="app"]/section/section/main/div[3]/div[5]/div/div[2]/div/div/div/form/div[1]/div[2]/div/div/div/div[1]/input')
    # driver.click('xpath', '/html/body/div[7]/div[1]/div[1]/ul/li/span[text()="小车"]')
    #
    # driver.click('xpath', "//input[contains(@placeholder,'请选择车辆动力类型')]")
    # driver.click('xpath', '/html/body/div[8]/div[1]/div[1]/ul/li/span[text()="燃油"]')
    #
    # driver.click('xpath', "//input[contains(@placeholder,'请选择车辆所有人')]")
    # driver.click('xpath', '/html/body/div[9]/div[1]/div[1]/ul/li/span[text()="单位"]')
    #
    # driver.input('xpath',
    #              '//*[@id="app"]/section/section/main/div[3]/div[5]/div/div[2]/div/div/div/form/div[2]/div[3]/div/div/div/input',
    #              'minzi')
    driver.clear('xpath',
                 '//*[@id="app"]/section/section/main/div[3]/div[5]/div/div[2]/div/div/div/form/div[3]/div[1]/div/div/div/input')
    driver.input('xpath',
                 '//*[@id="app"]/section/section/main/div[3]/div[5]/div/div[2]/div/div/div/form/div[3]/div[1]/div/div/div/input',
                 '15214141212')

    # driver.click('xpath', "//input[contains(@placeholder,'开始时间')]")
    # driver.click('xpath', '/html/body/div[10]/div[1]/div/div[1]/table/tbody/tr[3]/td[4]/div/span')
    # driver.click('xpath', '/html/body/div[10]/div[1]/div/div[2]/table/tbody/tr[5]/td[7]/div/span')

    # 保存
    driver.click('xpath',
                 '//*[@id="app"]/section/section/main/div[3]/div[5]/div/div[2]/div/div/div/form/div[5]/button/span')

    res = {'code': 0, 'message': 'UPDATE SUCCESS 更新成功'}
    logger.info(res)
    print(res)
    return res


def web_delete_black_list_func(driver, parajson, logger):
    """
    done
    :param driver:
    :param parajson:
    :return:
    """
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # time.sleep(200)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[4]')

    driver.input('xpath', "//input[@placeholder='请输入车牌号码']", paradic['car_no'])
    # 查询
    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/form/div[3]/div/button[1]/span')
    # 删除
    driver.click('xpath',
                 '//*[@id="app"]/section/section/main/div[3]/div[3]/div[3]/table/tbody/tr/td[12]/div/button[3]/span')
    driver.click('xpath', '/html/body/div[2]/div/div[3]/button[2]/span')

    res = {'code': 0, 'message': 'DELETE SUCCESS 删除成功'}
    logger.info(res)
    print(res)
    return res


def web_get_white_auth_func(driver, parajson, logger):
    """
    done
    :param driver:
    :param parajson:
    :return:
    """
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # time.sleep(200)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')
    driver.click('xpath', "//div[@id='tab-parkinglotapp-whitelistmgmt-whitelistauthrule']")

    driver.input('xpath', '//*[@id="whiteListauthrule"]/div[1]/div[1]/section/form/div[1]/div/div/input', 'rulename')

    # 查询
    driver.click('xpath', '//*[@id="whiteListauthrule"]/div[1]/div[1]/section/form/div[3]/div/button[1]/span')

    res = {'code': 0, 'message': 'GET SUCCESS 查询成功'}
    logger.info(res)
    print(res)
    return res


def web_add_white_auth_func(driver, parajson, logger):
    """
    done
    :param driver:
    :param parajson:
    :return:
    """
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # time.sleep(200)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')
    driver.click('xpath', "//div[@id='tab-parkinglotapp-whitelistmgmt-whitelistauthrule']")
    # 添加
    driver.click('xpath', '//*[@id="whiteListauthrule"]/div[1]/section/button[1]/span')

    driver.input('xpath', "//input[@placeholder='请输入规则名称']", paradic['rule_name'])

    for i in range(len(paradic['rule_channel']['auth_list'])):
        driver.click('xpath', '//*[@id="addCars"]/form/div[2]/div/div/button/span')

        driver.click('xpath', '/html/body/div[2]/div/div[2]/form/div[1]/div/div/div[1]/input')
        driver.click('xpath', '/html/body/div[4]/div[1]/div[1]/ul/li[6]/span')

        driver.click('xpath', '/html/body/div[2]/div/div[2]/form/div[2]/div/div/div[1]/input')
        driver.click('xpath', '/html/body/div[5]/div[1]/div[1]/ul/li[1]/span')

        driver.click('xpath', '/html/body/div[2]/div/div[2]/form/div[3]/div/div/div[1]/div/div[2]/input')
        driver.click('xpath', '/html/body/div[6]/div[1]/div[1]/ul/li[3]/span')
        driver.click('xpath', '/html/body/div[2]/div/div[2]/form/div[3]')

        driver.click('xpath', '/html/body/div[2]/div/div[2]/form/div[3]/div/div/div[2]/div/div/div/div[1]/div/input')
        driver.clear('xpath', '/html/body/div[2]/div/div[2]/form/div[3]/div/div/div[2]/div/div/div/div[1]/div/input')
        driver.input('xpath', '/html/body/div[2]/div/div[2]/form/div[3]/div/div/div[2]/div/div/div/div[1]/div/input',
                     paradic['rule_channel']['auth_list'][i]['begin_time'])
        driver.click('xpath', '/html/body/div[7]/div[2]/button[2]')

        driver.click('xpath', '/html/body/div[2]/div/div[2]/form/div[3]/div/div/div[2]/div/div/div/div[3]/div/input')
        driver.clear('xpath', '/html/body/div[2]/div/div[2]/form/div[3]/div/div/div[2]/div/div/div/div[3]/div/input')
        driver.input('xpath', '/html/body/div[2]/div/div[2]/form/div[3]/div/div/div[2]/div/div/div/div[3]/div/input',
                     paradic['rule_channel']['auth_list'][i]['end_time'])
        driver.click('xpath', '/html/body/div[8]/div[2]/button[2]')
        # 保存
        # time.sleep(20)
        driver.click('xpath', '/html/body/div[2]/div/div[2]/form/div[4]/div/button/span')
        time.sleep(1)

    driver.click('xpath', '//*[@id="addCars"]/form/div[4]/div/button[2]/span')
    time.sleep(2)
    res = {'code': 0, 'message': 'ADD SUCCESS 添加成功'}
    logger.info(res)
    return res


def web_update_white_auth_func(driver, parajson, logger):
    """
    done
    :param driver:
    :param parajson:
    :return:
    """
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # time.sleep(200)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')
    driver.click('xpath', "//div[@id='tab-parkinglotapp-whitelistmgmt-whitelistauthrule']")

    driver.input('xpath', '//*[@id="whiteListauthrule"]/div[1]/div[1]/section/form/div[1]/div/div/input',
                 paradic['rule_name'])

    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')
    # driver.click('xpath', "//div[@id='tab-parkinglotapp-whitelistmgmt-whitelistauthrule']")
    # 查询
    driver.click('xpath', '//*[@id="whiteListauthrule"]/div[1]/div[1]/section/form/div[3]/div/button[1]/span')
    # 编辑
    driver.click('xpath',
                 '//*[@id="whiteListauthrule"]/div[1]/div[2]/div[4]/div[2]/table/tbody/tr/td[8]/div/button[1]/span')

    driver.clear('xpath', '//*[@id="whiteListauthrule"]/div[1]/div[1]/section/form/div[1]/div/div/input')
    driver.input('xpath', '//*[@id="whiteListauthrule"]/div[1]/div[1]/section/form/div[1]/div/div/input',
                 paradic['rule_name'])

    # 保存
    driver.click('xpath', '//*[@id="addCars"]/form/div[4]/div/button[2]/span')

    res = {'code': 0, 'message': 'UPDATE SUCCESS 更新成功'}
    logger.info(res)
    return res


def web_delete_white_auth_func(driver, parajson, logger):
    """
    done
    :param driver:
    :param parajson:
    :return:
    """
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # time.sleep(200)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')
    driver.click('xpath', "//div[@id='tab-parkinglotapp-whitelistmgmt-whitelistauthrule']")

    driver.input('xpath', '//*[@id="whiteListauthrule"]/div[1]/div[1]/section/form/div[1]/div/div/input', 'rulename')

    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')
    # driver.click('xpath', "//div[@id='tab-parkinglotapp-whitelistmgmt-whitelistauthrule']")
    # 查询
    driver.click('xpath', '//*[@id="whiteListauthrule"]/div[1]/div[1]/section/form/div[3]/div/button[1]/span')
    # 删除
    driver.click('xpath',
                 '//*[@id="whiteListauthrule"]/div[1]/div[2]/div[4]/div[2]/table/tbody/tr/td[8]/div/button[3]/span')
    driver.click('xpath', '/html/body/div[8]/div/div[3]/button[2]/span')

    res = {'code': 0, 'message': 'DELETE SUCCESS 删除成功'}
    logger.info(res)
    print(res)
    return res


def web_get_white_list_func(driver, parajson, logger):
    """
    done
    :param driver:
    :param parajson:
    :return:
    """
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # time.sleep(200)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')

    if paradic['car_no']:
        driver.input('xpath', '//*[@id="white-list-car"]/div[1]/div[1]/section/form/div[1]/div/div/input',
                     paradic['car_no'])

    if paradic['list_type']:
        driver.click('xpath', '//*[@id="white-list-car"]/div[1]/div[1]/section/form/div[2]/div/div/div[1]/input')
        driver.click('xpath', '/html/body/div[2]/div[1]/div[1]/ul/li/span[text()="{}"]'.format(paradic['list_type']))

    if paradic['status_type']:
        driver.click('xpath', '//*[@id="white-list-car"]/div[1]/div[1]/section/form/div[3]/div/div/div[1]/input')
        driver.click('xpath', '/html/body/div[3]/div[1]/div[1]/ul/li/span[text()="{}"]'.format(paradic['status_type']))

    if paradic['con_name']:
        driver.input('xpath', '//*[@id="white-list-car"]/div[1]/div[1]/section/form/div[4]/div/div/input',
                     paradic['con_name'])

    if paradic['con_method']:
        driver.input('xpath', '//*[@id="white-list-car"]/div[1]/div[1]/section/form/div[5]/div/div/input',
                     paradic['con_method'])

    if paradic['rule_name']:
        driver.click('xpath', '//*[@id="white-list-car"]/div[1]/div[1]/section/form/div[6]/div/div/div[1]/input')
        driver.click('xpath', '/html/body/div[4]/div[1]/div[1]/ul/li/span[text()="{}"]'.format(paradic['rule_name']))
    # 查询
    driver.click('xpath', '//*[@id="white-list-car"]/div[1]/div[1]/section/form/div[7]/div/button[1]/span')
    time.sleep(2)
    res_text = driver.get_element_text('xpath',
                                       '//*[@id="white-list-car"]/div[1]/div[2]/div/div[3]/table/tbody/tr[1]/td[3]/div')

    if paradic['car_no'] in res_text:
        res = {'code': 0, 'message': 'GET SUCCESS 查询成功'}
        logger.info(res)
    else:
        res = {'code': -1, 'message': 'GET Fail 查询失败'}
        raise AssertionError(res)

    return res


def web_add_white_list_func(driver, parajson, logger):
    """
    done
    :param driver:
    :param parajson:
    :return:
    """
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # time.sleep(200)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')

    # 添加
    driver.click('xpath', '//*[@id="white-list-car"]/div[1]/section/button[1]/span')

    driver.input('xpath', "//input[@placeholder='请输入车牌号码']", paradic['car_no'])

    driver.click('xpath', '//*[@id="whitelistcar"]/form/div[2]/div/div/div[1]/input')
    driver.click('xpath', '/html/body/div[3]/div[1]/div[1]/ul/li/span[text()="{}"]'.format(paradic['list_type']))

    driver.click('xpath', '//*[@id="whitelistcar"]/form/div[3]/div/div/div[1]/input')
    driver.click('xpath', '/html/body/div[4]/div[1]/div[1]/ul/li/span[text()="{}"]'.format(paradic['car_type']))

    driver.click('xpath', '//*[@id="whitelistcar"]/form/div[4]/div/div/div[1]/input')
    driver.click('xpath', '/html/body/div[5]/div[1]/div[1]/ul/li/span[text()="{}"]'.format(paradic['move_type']))

    driver.click('xpath', '//*[@id="whitelistcar"]/form/div[5]/div/div/div[1]/input')
    driver.click('xpath', '/html/body/div[6]/div[1]/div[1]/ul/li/span[text()="{}"]'.format(paradic['car_own_type']))

    driver.input('xpath', '//*[@id="whitelistcar"]/form/div[6]/div/div/input', paradic['con_name'])

    driver.input('xpath', '//*[@id="whitelistcar"]/form/div[7]/div/div/input', paradic['con_method'])

    driver.click('xpath', "//input[@placeholder='开始日期']")
    driver.click('xpath', '/html/body/div[7]/div[1]/div/div[1]/table/tbody/tr[2]/td[3]/div/span')
    driver.click('xpath', '/html/body/div[7]/div[1]/div/div[2]/table/tbody/tr[6]/td[7]/div/span')

    driver.click('xpath', '//*[@id="whitelistcar"]/form/div[10]/div/div/div[1]/input')
    driver.click('xpath', '/html/body/div[8]/div[1]/div[1]/ul/li[1]/span')
    # 保存
    driver.click('xpath', '//*[@id="whitelistcar"]/form/div[11]/div/button[2]/span')

    time.sleep(3)

    res_visible = driver.element_should_not_be_visible('xpath', '//*[@id="white-list-car"]/div[2]/div/div[1]')
    res_visible = json.loads(res_visible)
    if res_visible['flag'] == 'True' and paradic['flag'] == 'True':
        res_text = driver.get_element_text('xpath',
                                           '//*[@id="white-list-car"]/div[1]/div[2]/div/div[3]/table/tbody/tr[1]/td[3]/div')

        if res_text == paradic['car_no']:
            res = {'code': 0, 'message': '{} ADD SUCCESS 添加成功'.format(paradic['car_no'])}
            logger.info(res)
        else:
            res = {'code': -1, 'message': '{} ADD FAIL 添加失败'.format(paradic['car_no'])}
            logger.info(res)
            raise AssertionError(res)
    elif res_visible['flag'] == 'True' and paradic['flag'] == 'False':
        raise AssertionError('添加失败')
    elif res_visible['flag'] == 'False' and paradic['flag'] == 'False':
        logger.info('反例 添加失败 用例 PASS')
    else:
        raise AssertionError('添加失败')


def web_update_white_list_func(driver, parajson, logger):
    """
    done
    :param driver:
    :param parajson:
    :return:
    """
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # time.sleep(200)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')

    driver.input('xpath', '//*[@id="white-list-car"]/div[1]/div[1]/section/form/div[1]/div/div/input',
                 paradic['car_no'])

    # driver.click('xpath', '//*[@id="white-list-car"]/div[1]/div[1]/section/form/div[2]/div/div/div[1]/input')
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')
    #
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')
    #
    # driver.input('xpath', "//input[@id='ruleName']", 'myrule')
    #
    # driver.input('xpath', "//input[@id='ruleName']", 'myrule')
    #
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')
    # 查询
    driver.click('xpath', '//*[@id="white-list-car"]/div[1]/div[1]/section/form/div[7]/div/button[1]/span')
    time.sleep(1)
    # 编辑
    driver.click('xpath',
                 '//*[@id="white-list-car"]/div[1]/div[2]/div/div[4]/div[2]/table/tbody/tr/td[13]/div/button[1]/span')

    # driver.click('xpath', '//*[@id="whitelistcar"]/form/div[2]/div/div/div[1]/input')
    # driver.click('xpath', '/html/body/div[3]/div[1]/div[1]/ul/li/span[text()="行政车辆"]')
    #
    # driver.click('xpath', '//*[@id="whitelistcar"]/form/div[3]/div/div/div[1]/input')
    # driver.click('xpath', '/html/body/div[4]/div[1]/div[1]/ul/li/span[text()="小车"]')
    #
    # driver.click('xpath', '//*[@id="whitelistcar"]/form/div[4]/div/div/div[1]/input')
    # driver.click('xpath', '/html/body/div[5]/div[1]/div[1]/ul/li/span[text()="燃油"]')
    #
    # driver.click('xpath', '//*[@id="whitelistcar"]/form/div[5]/div/div/div[1]/input')
    # driver.click('xpath', '/html/body/div[6]/div[1]/div[1]/ul/li/span[text()="个人"]')

    driver.clear('xpath', '//*[@id="whitelistcar"]/form/div[6]/div/div/input')
    driver.input('xpath', '//*[@id="whitelistcar"]/form/div[6]/div/div/input', paradic['con_name'])

    # driver.clear('xpath', '//*[@id="whitelistcar"]/form/div[7]/div/div/input')
    # driver.input('xpath', '//*[@id="whitelistcar"]/form/div[7]/div/div/input', '13113131311')
    #
    # driver.click('xpath', "//input[@placeholder='开始日期']")
    # driver.click('xpath', '/html/body/div[7]/div[1]/div/div[1]/table/tbody/tr[2]/td[3]/div/span')
    # driver.click('xpath', '/html/body/div[7]/div[1]/div/div[2]/table/tbody/tr[6]/td[7]/div/span')
    #
    # driver.click('xpath', '//*[@id="whitelistcar"]/form/div[10]/div/div/div[1]/input')
    # driver.click('xpath', '/html/body/div[8]/div[1]/div[1]/ul/li[1]/span')
    # 保存
    driver.click('xpath', '//*[@id="whitelistcar"]/form/div[11]/div/button[2]/span')

    res = {'code': 0, 'message': 'UPDATE SUCCESS 更新成功'}
    logger.info(res)
    print(res)
    return res


def web_delete_white_list_func(driver, parajson, logger):
    """
    done
    :param driver:
    :param parajson:
    :return:
    """
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # time.sleep(200)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')

    driver.input('xpath', '//*[@id="white-list-car"]/div[1]/div[1]/section/form/div[1]/div/div/input',
                 paradic['car_no'])

    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')
    #
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')
    #
    # driver.input('xpath', "//input[@id='ruleName']", 'myrule')
    #
    # driver.input('xpath', "//input[@id='ruleName']", 'myrule')
    #
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')
    # 查询
    driver.click('xpath', '//*[@id="white-list-car"]/div[1]/div[1]/section/form/div[7]/div/button[1]/span')

    # 删除
    driver.click('xpath',
                 '//*[@id="white-list-car"]/div[1]/div[2]/div/div[4]/div[2]/table/tbody/tr[1]/td[13]/div//button/span[text()="删除"]')
    driver.click('xpath', '/html/body/div[2]/div/div[3]/button[2]')

    time.sleep(2)

    res_visible = driver.element_should_not_be_visible('xpath',
                                                       '//*[@id="white-list-car"]/DIV[1]/DIV[2]/DIV/DIV[3]/TABLE/TBODY/TR/TD[1]')
    res_visible = json.loads(res_visible)
    if res_visible['flag'] == 'True' and paradic['flag'] == 'True':
        res = {'code': 0, 'message': '{} 删除 SUCCESS 删除成功'.format(paradic['car_no'])}
        logger.info(res)
    elif res_visible['flag'] == 'True' and paradic['flag'] == 'False':
        raise AssertionError('删除失败')
    elif res_visible['flag'] == 'False' and paradic['flag'] == 'False':
        logger.info('反例 删除失败 用例 PASS')
    else:
        raise AssertionError('删除失败')


def web_piliang_delete_white_list_func(driver, parajson, logger):
    """
    done
    :param driver:
    :param parajson:
    :return:
    """
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # time.sleep(200)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')

    driver.input('xpath', '//*[@id="white-list-car"]/div[1]/div[1]/section/form/div[1]/div/div/input',
                 paradic['car_no'])

    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')
    #
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')
    #
    # driver.input('xpath', "//input[@id='ruleName']", 'myrule')
    #
    # driver.input('xpath', "//input[@id='ruleName']", 'myrule')
    #
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')
    # 查询
    driver.click('xpath', '//*[@id="white-list-car"]/div[1]/div[2]/div/div[2]/table/thead/tr/th[1]/div/label/span/span')

    # 批量删除
    if paradic['is_checked'] == 'True':
        driver.click('xpath', '//*[@id="white-list-car"]/div[1]/section/button[2]/span')
    driver.click('xpath', '/html/body/div[2]/div/div[3]/button[2]/span')

    time.sleep(2)

    res_visible = driver.element_should_not_be_visible('xpath',
                                                       '//*[@id="white-list-car"]/DIV[1]/DIV[2]/DIV/DIV[3]/TABLE/TBODY/TR/TD[1]')
    res_visible = json.loads(res_visible)
    if res_visible['flag'] == 'True' and paradic['flag'] == 'True':
        res = {'code': 0, 'message': '{} 删除 SUCCESS 删除成功'.format(paradic['car_no'])}
        logger.info(res)
    elif res_visible['flag'] == 'True' and paradic['flag'] == 'False':
        raise AssertionError('删除失败')
    elif res_visible['flag'] == 'False' and paradic['flag'] == 'False':
        logger.info('反例 删除失败 用例 PASS')
    else:
        raise AssertionError('删除失败')


def web_auth_white_list_func(driver, parajson, logger):
    """
    done
    :param driver:
    :param parajson:
    :return:
    """
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # time.sleep(200)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')

    driver.input('xpath',
                 "/html[1]/body[1]/div[1]/section[1]/section[1]/main[1]/div[3]/div[1]/div[1]/section[1]/form[1]/div[1]/div[1]/div[1]/input[1]",
                 paradic['car_no'])

    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')
    #
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')
    #
    # driver.input('xpath', "//input[@id='ruleName']", 'myrule')
    #
    # driver.input('xpath', "//input[@id='ruleName']", 'myrule')
    #
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')
    # 查询
    driver.click('xpath', '//*[@id="white-list-car"]/div[1]/div[1]/section/form/div[7]/div/button[1]/span')
    time.sleep(2)
    # 授权
    driver.click('xpath',
                 '//*[@id="white-list-car"]/div[1]/div[2]/div/div[4]/div[2]/table/tbody/tr/td[13]/div/button[4]')
    driver.click('xpath', '/html/body/div[2]/div/div[3]/button[2]/span')

    time.sleep(2)
    res_text = driver.get_element_text('xpath',
                                       '//*[@id="white-list-car"]/div[1]/div[2]/div/div[3]/table/tbody/tr[1]/td[10]/div')
    if res_text['msg'] == '已授权':
        res = {'code': 0, 'message': 'AUTH SUCCESS 授权成功'}
        logger.info(res)
    else:
        res = {'code': -1, 'message': '{} AUTH FAIL 授权失败'.format(paradic['car_no'])}
        logger.info(res)
        raise AssertionError(res)
    return res


def web_piliang_auth_white_list_func(driver, parajson, logger):
    """
    done
    :param driver:
    :param parajson:
    :return:
    """
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # time.sleep(200)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')

    driver.input('xpath',
                 "/html[1]/body[1]/div[1]/section[1]/section[1]/main[1]/div[3]/div[1]/div[1]/section[1]/form[1]/div[1]/div[1]/div[1]/input[1]",
                 paradic['car_no'])

    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')
    #
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')
    #
    # driver.input('xpath', "//input[@id='ruleName']", 'myrule')
    #
    # driver.input('xpath', "//input[@id='ruleName']", 'myrule')
    #
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')
    # 查询
    driver.click('xpath', '//*[@id="white-list-car"]/div[1]/div[1]/section/form/div[7]/div/button[1]/span')
    time.sleep(2)
    # 批量授权
    if paradic['is_checked'] == "True":
        driver.click('xpath',
                     '//*[@id="white-list-car"]/div[1]/div[2]/div/div[2]/table/thead/tr/th[1]/div/label/span/span')
    driver.click('xpath', '/html/body/div[2]/div/div[3]/button[2]')

    time.sleep(2)
    res_text = driver.get_element_text('xpath',
                                       '//*[@id="white-list-car"]/div[1]/div[2]/div/div[3]/table/tbody/tr[1]/td[10]/div')
    if res_text['msg'] == '已授权':
        res = {'code': 0, 'message': 'AUTH SUCCESS 授权成功'}
        logger.info(res)
    else:
        res = {'code': -1, 'message': '{} AUTH FAIL 授权失败'.format(paradic['car_no'])}
        logger.info(res)
        raise AssertionError(res)
    return res


def web_unauth_white_list_func(driver, parajson, logger):
    """
    done
    :param driver:
    :param parajson:
    :return:
    """
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # time.sleep(200)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')

    driver.input('xpath',
                 "/html[1]/body[1]/div[1]/section[1]/section[1]/main[1]/div[3]/div[1]/div[1]/section[1]/form[1]/div[1]/div[1]/div[1]/input[1]",
                 paradic['car_no'])

    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')
    #
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')
    #
    # driver.input('xpath', "//input[@id='ruleName']", 'myrule')
    #
    # driver.input('xpath', "//input[@id='ruleName']", 'myrule')
    #
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[2]')
    # 查询
    driver.click('xpath', '//*[@id="white-list-car"]/div[1]/div[1]/section/form/div[7]/div/button[1]/span')
    # 取消授权
    driver.click('xpath',
                 '//*[@id="white-list-car"]/DIV[1]/DIV[2]/DIV/DIV[4]/DIV[2]/TABLE/TBODY/TR/TD[13]/DIV/BUTTON[3]/SPAN')
    driver.click('xpath', '/HTML/BODY/DIV[2]/DIV/DIV[3]/BUTTON[2]/SPAN')

    res = {'code': 0, 'message': 'UNAUTH SUCCESS 取消授权成功'}
    logger.info(res)
    print(res)
    return res


def web_get_io_rule_func(driver, parajson, logger):
    """
    done
    :param driver:
    :param parajson:
    :return:
    """
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # time.sleep(200)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[1]')

    driver.click('xpath', "//div[@id='tab-parkinglotapp-parkingbaseconfig-inoutrule']")

    driver.input('xpath', "//input[@id='ruleName']", paradic['rule_name'])
    # 点击查询
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[1]')


def web_add_io_rule_func(driver, parajson, logger):
    """
    done
    :param driver:
    :param parajson:
    :return:
    """
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # time.sleep(200)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[1]')

    driver.click('xpath', "//div[@id='tab-parkinglotapp-parkingbaseconfig-inoutrule']")
    # 添加
    driver.click('xpath', '//*[@id="rule"]/section/button[1]/span')

    driver.input('xpath', '//*[@id="editeRuleDialog"]/div/div[2]/form/div[1]/div/div/input',
                 paradic['rule_name'])

    # driver.click('xpath', '//*[@id="editeRuleDialog"]/div/div[2]/form/div[2]/div/div/div[1]/input')
    # time.sleep(1)
    # driver.click('xpath', '/html/body/div[3]/div[1]/div[1]/ul/li/span')
    # 保存
    driver.click('xpath', '//*[@id="editeRuleDialog"]/div/div[2]/form/div[5]/div/button[2]/span')

    res = {'code': 0, 'message': 'ADD SUCCESS 添加成功'}
    logger.info(res)
    print(res)
    return res


def web_update_io_rule_func(driver, parajson, logger):
    """
    done
    :param driver:
    :param parajson:
    :return:
    """
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # time.sleep(200)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[1]')

    driver.click('xpath', "//div[@id='tab-parkinglotapp-parkingbaseconfig-inoutrule']")

    driver.input('xpath', "//input[@id='ruleName']", paradic['old_rule_name'])
    driver.click('xpath', '//*[@id="rule"]/div[1]/div/form/div[2]/div/button/span')
    time.sleep(2)
    # 编辑
    driver.click('xpath', '//*[@id="rule"]/div[2]/div[3]/table/tbody/tr/td[8]/div/button[2]/span')
    time.sleep(1)
    driver.clear('xpath', '//*[@id="editeRuleDialog"]/div/div[2]/form/div[1]/div/div/input')
    driver.input('xpath', '//*[@id="editeRuleDialog"]/div/div[2]/form/div[1]/div/div/input',
                 paradic['new_rule_name'])

    # 保存
    driver.click('xpath', '//*[@id="editeRuleDialog"]/div/div[2]/form/div[5]/div/button[2]/span')

    res = {'code': 0, 'message': 'UPDATE SUCCESS 更新成功'}
    logger.info(res)
    print(res)
    return res


def web_delete_io_rule_func(driver, parajson, logger):
    """
    done
    :param driver:
    :param parajson:
    :return:
    """
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # time.sleep(200)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[1]')
    driver.click('xpath', "//div[@id='tab-parkinglotapp-parkingbaseconfig-inoutrule']")

    driver.input('xpath', "//input[@id='ruleName']", paradic['rule_name'])
    # 点击查询
    driver.click('xpath', '//*[@id="rule"]/div[1]/div/form/div[2]/div/button/span')
    # 删除
    driver.click('xpath', '//*[@id="rule"]/div[2]/div[3]/table/tbody/tr[1]/td[8]/div/button[3]/span')
    driver.click('xpath', '/html/body/div[2]/div/div[3]/button[2]/span')

    res = {'code': 0, 'message': 'DELETE SUCCESS 删除成功'}
    logger.info(res)
    print(res)
    return res


def web_get_car_io_rule_func(driver, parajson, logger):
    """
    done
    :param driver:
    :param parajson:
    :return:
    """
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # time.sleep(200)

    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    # driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[6]')
    # 点击停车场管理
    driver.click('xpath', '//*[@id="app"]//div//div//li[1]//div[1]')
    # 点击数据统计
    driver.click('xpath', '//li[1]//ul[1]//li[6]')


    # driver.click('xpath', "//div[@id='tab-parkinglotapp-statistics-outrecord']")
    # 点击出入场记录
    driver.click('xpath', "//div[@id='tab-parkinglotapp-statistics-outrecord']")

    # driver.input('xpath', "//input[@placeholder='请输入车场名称']", paradic['park_name'])
    #
    # driver.click('xpath', "//input[@placeholder='车辆类型']")
    # driver.click('xpath', '/html/body/div[2]/div[1]/div[1]/ul/li/span[text()="{}"]'.format(paradic['car_type']))

    driver.input('xpath', "//input[@placeholder='请输入车牌号']", paradic['car_number'])

    # driver.click('xpath', "//input[@placeholder='入场开闸方式']")
    # driver.click('xpath', '/html/body/div[3]/div[1]/div[1]/ul/li/span[text()="{}"]'.format(paradic['in_type']))
    #
    # driver.click('xpath', "//input[@placeholder='出场开闸方式']")
    # driver.click('xpath', '/html/body/div[4]/div[1]/div[1]/ul/li/span[text()="{}"]'.format(paradic['out_type']))
    #
    # driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/section/form/div[6]/div/div/input[1]')
    # driver.clear('xpath', '/html/body/div[5]/div[1]/div[2]/div[1]/span[1]/span[1]/div/input')
    # driver.input('xpath', '/html/body/div[5]/div[1]/div[2]/div[1]/span[1]/span[1]/div/input',
    #              paradic['in_time_start'][:10])
    # driver.clear('xpath', '/html/body/div[5]/div[1]/div[2]/div[1]/span[1]/span[2]/div[1]/input')
    # driver.input('xpath', '/html/body/div[5]/div[1]/div[2]/div[1]/span[1]/span[2]/div[1]/input',
    #              paradic['in_time_start'][11:])
    # driver.clear('xpath', '/html/body/div[5]/div[1]/div[2]/div[1]/span[3]/span[1]/div/input')
    # driver.input('xpath', '/html/body/div[5]/div[1]/div[2]/div[1]/span[3]/span[1]/div/input',
    #              paradic['in_time_end'][:10])
    # driver.clear('xpath', '/html/body/div[5]/div[1]/div[2]/div[1]/span[3]/span[2]/div[1]/input')
    # driver.input('xpath', '/html/body/div[5]/div[1]/div[2]/div[1]/span[3]/span[2]/div[1]/input',
    #              paradic['in_time_end'][11:])
    # driver.click('xpath', '/html/body/div[5]/div[2]/button[2]/span')
    #
    # driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/section/form/div[7]/div/div/input[1]')
    # driver.clear('xpath', '/html/body/div[6]/div[1]/div[2]/div[1]/span[1]/span[1]/div/input')
    # driver.input('xpath', '/html/body/div[6]/div[1]/div[2]/div[1]/span[1]/span[1]/div/input',
    #              paradic['out_time_start'][:10])
    # driver.clear('xpath', '/html/body/div[6]/div[1]/div[2]/div[1]/span[1]/span[2]/div[1]/input')
    # driver.input('xpath', '/html/body/div[6]/div[1]/div[2]/div[1]/span[1]/span[2]/div[1]/input',
    #              paradic['out_time_start'][11:])
    # driver.clear('xpath', '/html/body/div[6]/div[1]/div[2]/div[1]/span[3]/span[1]/div/input')
    # driver.input('xpath', '/html/body/div[6]/div[1]/div[2]/div[1]/span[3]/span[1]/div/input',
    #              paradic['out_time_end'][:10])
    # driver.clear('xpath', '/html/body/div[6]/div[1]/div[2]/div[1]/span[3]/span[2]/div[1]/input')
    # driver.input('xpath', '/html/body/div[6]/div[1]/div[2]/div[1]/span[3]/span[2]/div[1]/input',
    #              paradic['out_time_end'][11:])
    # driver.click('xpath', '/html/body/div[6]/div[2]/button[2]/span')

    # driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/section/form/div[8]/div/button/span')
    driver.click('xpath', "//div[@class='el-form-item__content']//button[@class='el-button el-button--primary']//span")

    time.sleep(2)
    pt = driver.get_element_text('xpath',
                                 '//*[@id="app"]/section/section/main/div[3]/section/div[1]/div/div[3]/table/tbody/tr[1]/td[11]/div')

    logger.info('停车时长：{}'.format(pt))

    mo = driver.get_element_text('xpath',
                                 '//*[@id="app"]/section/section/main/div[3]/section/div[1]/div/div[3]/table/tbody/tr[1]/td[14]/div')

    logger.info('实缴金额：{} 元'.format(mo))

    res = {'code': 0, 'message': 'GET SUCCESS 查询成功'}
    logger.info(res)
    print(res)
    return res


def web_get_nocar_io_rule_func(driver, parajson, logger):
    """
    done
    :param driver:
    :param parajson:
    :return:
    """
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # time.sleep(200)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[6]')

    driver.click('xpath', "//div[@id='tab-parkinglotapp-statistics-nonMotorOutRecord']")

    driver.click('xpath', '//*[@id="non-motor-out-record"]/div[1]/form/div[1]/div/div/input[1]')
    driver.clear('xpath', '/html/body/div[2]/div[1]/div[2]/div[1]/span[1]/span[1]/div/input')
    driver.input('xpath', '/html/body/div[2]/div[1]/div[2]/div[1]/span[1]/span[1]/div/input',
                 paradic['time_start'][:10])
    driver.clear('xpath', '/html/body/div[2]/div[1]/div[2]/div[1]/span[1]/span[2]/div[1]/input')
    driver.input('xpath', '/html/body/div[2]/div[1]/div[2]/div[1]/span[1]/span[2]/div[1]/input',
                 paradic['time_start'][11:])
    driver.clear('xpath', '/html/body/div[2]/div[1]/div[2]/div[1]/span[3]/span[1]/div/input')
    driver.input('xpath', '/html/body/div[2]/div[1]/div[2]/div[1]/span[3]/span[1]/div/input',
                 paradic['time_end'][:10])
    driver.clear('xpath', '/html/body/div[2]/div[1]/div[2]/div[1]/span[3]/span[2]/div[1]/input')
    driver.input('xpath', '/html/body/div[2]/div[1]/div[2]/div[1]/span[3]/span[2]/div[1]/input',
                 paradic['time_end'][11:])
    driver.click('xpath', '/html/body/div[2]/div[2]/button[2]/span')

    driver.click('xpath', '//*[@id="non-motor-out-record"]/div[1]/form/div[2]/div/div/div[1]/input')
    driver.click('xpath',
                 '/html/body/div[3]/div[1]/div[1]/ul/li/span[text()="{}"]'.format(paradic['type']))

    driver.input('xpath', "//input[@placeholder='请输入车牌号']", paradic['car_number'])

    driver.click('xpath', '//*[@id="non-motor-out-record"]/div[1]/form/div[4]/div/button[1]/span')

    res = {'code': 0, 'message': 'GET SUCCESS 查询成功'}
    logger.info(res)
    print(res)
    return res


def web_get_car_in_park_func(driver, parajson, logger):
    """
    done
    :param driver:
    :param parajson:
    :return:
    """
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # time.sleep(200)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[6]')

    driver.click('xpath', "//div[@id='tab-parkinglotapp-statistics-presentcars']")

    driver.input('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/section/form/div[1]/div/div/input',
                 paradic['park_name'])
    driver.input('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/section/form/div[2]/div/div/input',
                 paradic['car_number'])

    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/section/form/div[3]/div/div/div[1]/input')
    driver.click('xpath',
                 '/html/body/div[2]/div[1]/div[1]/ul/li/span[text()="{}"]'.format(paradic['car_type']))

    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/section/form/div[4]/div/div/div[1]/input')

    driver.click('xpath',
                 '/html/body/div[3]/div[1]/div[1]/ul/li/span[text()="{}"]'.format(paradic['open_type']))

    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/section/form/div[5]/div/div/input[1]')
    driver.clear('xpath', '/html/body/div[4]/div[1]/div[2]/div[1]/span[1]/span[1]/div/input')
    driver.input('xpath', '/html/body/div[4]/div[1]/div[2]/div[1]/span[1]/span[1]/div[1]/input',
                 paradic['in_time_start'][:10])
    driver.clear('xpath', '/html/body/div[4]/div[1]/div[2]/div[1]/span[1]/span[2]/div[1]/input')
    driver.input('xpath', '/html/body/div[4]/div[1]/div[2]/div[1]/span[1]/span[2]/div[1]/input',
                 paradic['in_time_start'][11:])
    driver.clear('xpath', '/html/body/div[4]/div[1]/div[2]/div[1]/span[3]/span[1]/div/input')
    driver.input('xpath', '/html/body/div[4]/div[1]/div[2]/div[1]/span[3]/span[1]/div/input',
                 paradic['in_time_end'][:10])
    driver.clear('xpath', '/html/body/div[4]/div[1]/div[2]/div[1]/span[3]/span[2]/div[1]/input')
    driver.input('xpath', '/html/body/div[4]/div[1]/div[2]/div[1]/span[3]/span[2]/div[1]/input',
                 paradic['in_time_end'][11:])
    driver.click('xpath', '/html/body/div[4]/div[2]/button[2]/span')

    # 查询
    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/section/form/div[6]/div/button[1]/span')

    res = {'code': 0, 'message': 'GET SUCCESS 查询成功'}
    logger.info(res)
    print(res)
    return res


def web_get_pay_record_func(driver, parajson, logger):
    """
    done
    :param driver:
    :param parajson:
    :return:
    """
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # time.sleep(200)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[6]')

    driver.click('xpath', "//div[@id='tab-parkinglotapp-statistics-payrecord']")

    driver.input('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/section/form/div[1]/div/div/input',
                 paradic['park_name'])

    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/section/form/div[2]/div/div/div/input')
    driver.click('xpath',
                 '/html/body/div[2]/div[1]/div[1]/ul//li/span[text()="{}"]'.format(paradic['car_type']))

    driver.input('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/section/form/div[3]/div/div/input',
                 paradic['car_number'])

    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/section/form/div[4]/div/div/div[1]/input')
    driver.click('xpath',
                 "/html/body/div[3]/div[1]/div[1]/ul/li/span[text()='{}']".format(paradic['isin_park']))

    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/section/form/div[7]/div/div/input[1]')
    driver.clear('xpath', '/html/body/div[3]/div[1]/div[2]/div[1]/span[1]/span[1]/div/input')
    driver.input('xpath', '/html/body/div[3]/div[1]/div[2]/div[1]/span[1]/span[1]/div/input',
                 paradic['in_time_start'][:10])
    driver.clear('xpath', '/html/body/div[4]/div[1]/div[2]/div[1]/span[1]/span[2]/div[1]/input')
    driver.input('xpath', '/html/body/div[4]/div[1]/div[2]/div[1]/span[1]/span[2]/div[1]/input',
                 paradic['in_time_start'][11:])
    driver.clear('xpath', '/html/body/div[4]/div[1]/div[2]/div[1]/span[3]/span[1]/div/input')
    driver.input('xpath', '/html/body/div[4]/div[1]/div[2]/div[1]/span[3]/span[1]/div/input',
                 paradic['in_time_end'][:10])
    driver.clear('xpath', '/html/body/div[4]/div[1]/div[2]/div[1]/span[3]/span[2]/div[1]/input')
    driver.input('xpath', '/html/body/div[4]/div[1]/div[2]/div[1]/span[3]/span[2]/div[1]/input',
                 paradic['in_time_end'][11:])
    driver.click('xpath', '/html/body/div[4]/div[2]/button[2]/span')

    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/section/form/div[8]/div/div/input[1]')
    driver.clear('xpath', '/html/body/div[4]/div[1]/div[2]/div[1]/span[1]/span[1]/div/input')
    driver.input('xpath', '/html/body/div[4]/div[1]/div[2]/div[1]/span[1]/span[1]/div/input',
                 paradic['pay_time_start'][:10])
    driver.clear('xpath', '/html/body/div[4]/div[1]/div[2]/div[1]/span[1]/span[2]/div[1]/input')
    driver.input('xpath', '/html/body/div[4]/div[1]/div[2]/div[1]/span[1]/span[2]/div[1]/input',
                 paradic['pay_time_start'][11:])
    driver.clear('xpath', '/html/body/div[4]/div[1]/div[2]/div[1]/span[3]/span[1]/div/input')
    driver.input('xpath', '/html/body/div[4]/div[1]/div[2]/div[1]/span[3]/span[1]/div/input',
                 paradic['pay_time_end'][:10])
    driver.clear('xpath', '/html/body/div[4]/div[1]/div[2]/div[1]/span[3]/span[2]/div[1]/input')
    driver.input('xpath', '/html/body/div[4]/div[1]/div[2]/div[1]/span[3]/span[2]/div[1]/input',
                 paradic['pay_time_end'][11:])
    driver.click('xpath', '/html/body/div[5]/div[2]/button[2]/span')

    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/div[1]/section/form/div[7]/div/div/input[1]')
    driver.clear('xpath', '/html/body/div[6]/div[1]/div[2]/div[1]/span[1]/span[1]/div/input')
    driver.input('xpath', '/html/body/div[6]/div[1]/div[2]/div[1]/span[1]/span[1]/div/input',
                 paradic['out_time_start'][:10])
    driver.clear('xpath', '/html/body/div[6]/div[1]/div[2]/div[1]/span[1]/span[2]/div[1]/input')
    driver.input('xpath', '/html/body/div[6]/div[1]/div[2]/div[1]/span[1]/span[2]/div[1]/input',
                 paradic['out_time_start'][11:])
    driver.clear('xpath', '/html/body/div[6]/div[1]/div[2]/div[1]/span[3]/span[1]/div/input')
    driver.input('xpath', '/html/body/div[6]/div[1]/div[2]/div[1]/span[3]/span[1]/div/input',
                 paradic['out_time_end'][:10])
    driver.clear('xpath', '/html/body/div[6]/div[1]/div[2]/div[1]/span[3]/span[2]/div[1]/input')
    driver.input('xpath', '/html/body/div[6]/div[1]/div[2]/div[1]/span[3]/span[2]/div[1]/input',
                 paradic['out_time_end'][11:])
    driver.click('xpath', '/html/body/div[6]/div[2]/button[2]/span')

    driver.click('xpath', "//button[@class='el-button el-button--primary']//span")

    res = {'code': 0, 'message': 'GET SUCCESS 查询成功'}
    logger.info(res)
    print(res)
    return res


def web_get_pay_statistics_func(driver, parajson, logger):
    """
    done
    :param driver:
    :param parajson:
    :return:
    """
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[6]')

    driver.click('xpath', "//div[@id='tab-parkinglotapp-statistics-payCount']")

    driver.click('xpath', "//input[@placeholder='开始日期']")
    driver.clear('xpath', '/html/body/div[2]/div[1]/div[2]/div[1]/span[1]/span[1]/div/input')
    driver.input('xpath', '/html/body/div[2]/div[1]/div[2]/div[1]/span[1]/span[1]/div/input',
                 paradic['time_start'][:10])
    driver.clear('xpath', '/html/body/div[2]/div[1]/div[2]/div[1]/span[1]/span[2]/div[1]/input')
    driver.input('xpath', '/html/body/div[2]/div[1]/div[2]/div[1]/span[1]/span[2]/div[1]/input',
                 paradic['time_end'][11:])
    driver.clear('xpath', '/html/body/div[2]/div[1]/div[2]/div[1]/span[3]/span[1]/div/input')
    driver.input('xpath', '/html/body/div[2]/div[1]/div[2]/div[1]/span[3]/span[1]/div/input',
                 paradic['time_end'][:10])
    driver.clear('xpath', '/html/body/div[2]/div[1]/div[2]/div[1]/span[3]/span[2]/div[1]/input')
    driver.input('xpath', '/html/body/div[2]/div[1]/div[2]/div[1]/span[3]/span[2]/div[1]/input',
                 paradic['time_end'][11:])
    driver.click('xpath', '/html/body/div[2]/div[2]/button[2]/span')

    if paradic['type'] == '出口车辆缴费统计':
        driver.click('xpath', "//div[@id='tab-second']")
    # 查询
    driver.click('xpath', "//section[@class='record-main']//button[2]")

    res = {'code': 0, 'message': 'GET SUCCESS 查询成功'}
    logger.info(res)
    print(res)
    return res


def web_open_out_in_control_func(driver, parajson, logger):
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # time.sleep(200)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[5]')
    time.sleep(2)
    driver.input_tab_enter()


def web_man_fangxing_in_func(driver, parajson, logger):
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)

    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[5]')
    time.sleep(2)
    driver.input_tab_enter()

    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/section[1]/button[1]/span')

    driver.click('xpath',
                 '//*[@id="app"]/section/section/main/div[3]/div[2]/div/div[2]/div[2]/form/div[1]/div[1]/div/div/div[1]/input')
    driver.click('xpath', '/html/body/div[3]/div[1]/div[1]/ul/li[2]/span')
    driver.click('xpath',
                 '//*[@id="app"]/section/section/main/div[3]/div[2]/div/div[2]/div[2]/form/div[1]/div[2]/div/div/div[1]/input')
    driver.click('xpath', '/HTML/BODY/DIV[4]/DIV[1]/DIV[1]/UL/LI/SPAN')

    driver.click('xpath',
                 '//*[@id="app"]/SECTION/SECTION/main/DIV[3]/DIV[2]/DIV/DIV[2]/DIV[2]/FORM/DIV[1]/DIV[3]/DIV/DIV/INPUT')
    driver.input('xpath',
                 '//*[@id="app"]/SECTION/SECTION/main/DIV[3]/DIV[2]/DIV/DIV[2]/DIV[2]/FORM/DIV[1]/DIV[3]/DIV/DIV/INPUT',
                 paradic['car_num'])
    driver.click('xpath',
                 '//*[@id="app"]/SECTION/SECTION/main/DIV[3]/DIV[2]/DIV/DIV[2]/DIV[2]/FORM/DIV[1]/DIV[6]/DIV/DIV/DIV/INPUT')
    driver.click('xpath', '/HTML/BODY/DIV[5]/DIV[1]/DIV[1]/UL/LI[1]/SPAN')
    driver.click('xpath',
                 '//*[@id="app"]/SECTION/SECTION/main/DIV[3]/DIV[2]/DIV/DIV[2]/DIV[2]/FORM/DIV[2]/DIV/BUTTON[2]/SPAN')

    res = {'code': 0, 'message': 'GET SUCCESS 查询成功'}
    logger.info(res)
    return res


def web_man_fangxing_out_func(driver, parajson, logger):
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)

    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[5]')
    time.sleep(2)
    driver.input_tab_enter()

    driver.click('xpath', '//*[@id="app"]/SECTION/SECTION/main/DIV[2]/DIV')

    driver.click('xpath', '//*[@id="app"]/SECTION/SECTION/main/DIV[3]/SECTION[1]/BUTTON[2]/SPAN')

    driver.click('xpath',
                 '//*[@id="app"]/SECTION/SECTION/main/DIV[3]/DIV[2]/DIV/DIV[2]/DIV[2]/FORM/DIV[1]/DIV[1]/DIV/DIV/DIV[1]/INPUT')
    driver.click('xpath', '/HTML/BODY/DIV[3]/DIV[1]/DIV[1]/UL/LI[2]/SPAN')

    driver.click('xpath',
                 '//*[@id="app"]/SECTION/SECTION/main/DIV[3]/DIV[2]/DIV/DIV[2]/DIV[2]/FORM/DIV[1]/DIV[2]/DIV/DIV/DIV[1]/INPUT')
    driver.click('xpath', '/HTML/BODY/DIV[4]/DIV[1]/DIV[1]/UL/LI/SPAN')

    driver.click('xpath',
                 '//*[@id="app"]/SECTION/SECTION/main/DIV[3]/DIV[2]/DIV/DIV[2]/DIV[2]/FORM/DIV[1]/DIV[3]/DIV/DIV/INPUT')
    driver.input('xpath',
                 '//*[@id="app"]/SECTION/SECTION/main/DIV[3]/DIV[2]/DIV/DIV[2]/DIV[2]/FORM/DIV[1]/DIV[3]/DIV/DIV/INPUT',
                 paradic['car_num'])

    driver.click('xpath',
                 '//*[@id="app"]/SECTION/SECTION/main/DIV[3]/DIV[2]/DIV/DIV[2]/DIV[2]/FORM/DIV[1]/DIV[6]/DIV/DIV/DIV[1]/INPUT')
    driver.click('xpath', '/HTML/BODY/DIV[5]/DIV[1]/DIV[1]/UL/LI[1]/SPAN')
    driver.click('xpath',
                 '//*[@id="app"]/SECTION/SECTION/main/DIV[3]/DIV[2]/DIV/DIV[2]/DIV[2]/FORM/DIV[2]/DIV/BUTTON[2]/SPAN')

    # 开闸
    driver.click('xpath',
                 '//*[@id="app"]/SECTION/SECTION/main/DIV[3]/DIV[1]/DIV/DIV[2]/DIV[2]/DIV[2]/FORM/DIV[2]/DIV/BUTTON[1]/SPAN')

    res = {'code': 0, 'message': 'GET SUCCESS 查询成功'}
    logger.info(res)
    return res


def web_parkcar_func(driver, parajson, logger):
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)

    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[5]')

    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/section[1]/button[3]/span')
    driver.input('xpath',
                 '//*[@id="app"]/section/section/main/div[3]/div[6]/div/div[2]/div[2]/section[1]/form/div[1]/div/div/input',
                 paradic['car_card'])
    driver.click('xpath',
                 '//*[@id="app"]/section/section/main/div[3]/div[6]/div/div[2]/div[2]/section[1]/form/div[4]/div/button[1]/span')

    time.sleep(2)

    res_text = driver.get_element_text('xpath',
                                       '//*[@id="app"]/SECTION/SECTION/main/DIV[3]/DIV[6]/DIV/DIV[2]/DIV[2]/SECTION[2]/DIV[1]/DIV/DIV[3]/TABLE/TBODY/TR/TD[3]/DIV')

    if res_text == paradic['car_card']:
        res = {'code': 0, 'message': 'GET SUCCESS 查询成功'}
        logger.info(res)
    else:
        res = {'code': -1, 'message': 'GET FAIL 查询失败'}
        logger.info(res)
        raise AssertionError('该车牌未查询到')
    return res


def web_get_delete_car_func(driver, parajson, logger):
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # time.sleep(200)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[5]')
    driver.click('xpath', '//*[@id="app"]/section/section/main/div[3]/section[1]/button[4]/span')
    driver.input('xpath',
                 '//*[@id="app"]/section/section/main/div[3]/div[6]/div/div[2]/div[2]/section[1]/form/div[1]/div/div/input',
                 paradic['car_card'])
    driver.click('xpath',
                 '//*[@id="app"]/section/section/main/div[3]/div[6]/div/div[2]/div[2]/section[1]/form/div[3]/div/button[1]/span')

    in_time = driver.get_element_text('xpath',
                                      '//*[@id="app"]/section/section/main/div[3]/div[6]/div/div[2]/div[2]/section[2]/div[1]/div/div[3]/table/tbody/tr[1]/td[6]/div')
    del_time = driver.get_element_text('xpath',
                                       '//*[@id="app"]/section/section/main/div[3]/div[6]/div/div[2]/div[2]/section[2]/div[1]/div/div[3]/table/tbody/tr[1]/td[9]/div')

    logger.info('查询到的入场时间是：{}'.format(in_time))
    logger.info('查询到的移除时间是：{}'.format(del_time))


def web_get_park_info_func(driver, parajson, logger):
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # time.sleep(200)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[5]')

    lin_all_parknum = driver.get_element_text('xpath',
                                              '//*[@id="inout-right-cont"]/article[3]/div/div[3]/table/tbody/tr/td[1]/div[text()="{}"]/parent::td/parent::tr/td[2]/div'.format(
                                                  paradic['park_name']))
    lin_last_parknum = driver.get_element_text('xpath',
                                               '//*[@id="inout-right-cont"]/article[3]/div/div[3]/table/tbody/tr/td[1]/div[text()="{}"]/parent::td/parent::tr/td[3]/div/span'.format(
                                                   paradic['park_name']))

    logger.info('查询到的总车位数是：{}'.format(lin_all_parknum))
    logger.info('查询到的剩余车位是：{}'.format(lin_last_parknum))


def web_get_inout_park_info_func(driver, parajson, logger):
    parajson = json.dumps(parajson)
    paradic = json.loads(parajson)
    # time.sleep(200)
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/div')
    driver.click('xpath', '//*[@id="app"]/section/section/aside/div[2]/ul/li[1]/ul/li[5]')
    time.sleep(2)
    car_num = driver.get_element_text('xpath',
                                      '//*[@id="app"]/section/section/main/div[3]/section[3]/div/div[3]/table/tbody/tr/td[2]/div')
    card_num = driver.get_element_text('xpath',
                                       '//*[@id="app"]/section/section/main/div[3]/section[3]/div/div[3]/table/tbody/tr/td[3]/div')
    in_out_type = driver.get_element_text('xpath',
                                          '//*[@id="app"]/section/section/main/div[3]/section[3]/div/div[3]/table/tbody/tr/td[4]/div')
    car_type = driver.get_element_text('xpath',
                                       '//*[@id="app"]/section/section/main/div[3]/section[3]/div/div[3]/table/tbody/tr/td[5]/div')
    out_in_chan = driver.get_element_text('xpath',
                                          '//*[@id="app"]/section/section/main/div[3]/section[3]/div/div[3]/table/tbody/tr/td[6]/div')
    man_name = driver.get_element_text('xpath',
                                       '//*[@id="app"]/section/section/main/div[3]/section[3]/div/div[3]/table/tbody/tr/td[7]/div')
    in_time = driver.get_element_text('xpath',
                                      '//*[@id="app"]/section/section/main/div[3]/section[3]/div/div[3]/table/tbody/tr/td[8]/div')
    out_time = driver.get_element_text('xpath',
                                       '//*[@id="app"]/section/section/main/div[3]/section[3]/div/div[3]/table/tbody/tr/td[9]/div')
    rules = driver.get_element_text('xpath',
                                    '//*[@id="app"]/section/section/main/div[3]/section[3]/div/div[3]/table/tbody/tr/td[10]/div')
    online_money = driver.get_element_text('xpath',
                                           '//*[@id="app"]/section/section/main/div[3]/section[3]/div/div[3]/table/tbody/tr/td[11]/div')
    xianxia_money = driver.get_element_text('xpath',
                                            '//*[@id="app"]/section/section/main/div[3]/section[3]/div/div[3]/table/tbody/tr/td[12]/div')

    logger.info('查询到的线下收费金额是：{}'.format(xianxia_money))
    res = {'code': 0, 'message': 'GET SUCCESS 查询成功'}
    logger.info(res)
    print(res)
    return res


def asserts(st1, st2):
    if str(st1) == str(st2):
        return True
    else:
        return False


def login_web(driver, url):
    #登入官网门户网站
    driver.openurl(url)
    driver.click('xpath', '//*[@id="details-button"]')
    driver.click('xpath', '//*[@id="proceed-link"]')
    driver.element_should_contain('xpath', '//*[@id="amusementBook"]', '预订')
    time.sleep(1)


def booking_tickit(driver):
    #点击官网页面的预定按钮
    driver.click('xpath', '//*[@id="amusementBook"]')
    time.sleep(1)


def select_tickit(driver, xpath):
    # 列表中选择门票
    driver.click('xpath', xpath)
    time.sleep(1)


loc_save_trip= '//*[@id="banner-section"]/div/div/div[1]/div[2]/div/div/ul/li[1]/div/img[2]'

def click_play_lable(driver,xpath):
    # 点击首页的门票按钮
    driver.click('xpath',loc_save_trip)
    time.sleep(1)


if __name__ == "__main__":
    pass
    # logger = Logger()
    # driver = WebDriver(logger)
    # # driver.setup('chrome')
    # # driver.openurl("http://10.101.72.77:81/login")
    # # driver.input('xpath', "//input[@placeholder='账户名']", 'admin')
    # # driver.input('xpath', "//input[@placeholder='密码']", 'admin')
    # # time.sleep(8)