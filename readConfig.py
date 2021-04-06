# coding=utf-8
import os
import configparser
current_path = os.getcwd()


def get_config(section, key):
    config = configparser.ConfigParser()
    # 获取配置文件的真实路径
    # path = os.path.split(os.path.realpath(__file__))[0] + '\config.ini'
    path = os.path.join(current_path, 'config_file/config.ini')
    # print("获取配置文件的真实路径为："+path)
    config.read(path, encoding="utf-8")
    return config.get(section, key)


