# -*- coding: UTF-8 -*-
'''
@Author  ：程序员晚枫，B站/抖音/微博/小红书/公众号
@WeChat     ：CoderWanFeng
@Blog      ：www.python-office.com
@Date    ：2023/1/22 15:23
@Description     ：
'''

from pobaidu.core.ImageProcess import ImageProcess


def get_ImageProcess(configPath):
    ip = ImageProcess()
    ip.set_config(configPath)
    return ip


def colourize(img_path, output_path=r'./', configPath=None):
    ip = get_ImageProcess(configPath)
    file_data = ip.colourize(img_path)
    ip.save_file_content(filePath=output_path, fileData=file_data)


def selfieAnime(filePath, output_path=r'./', configPath=None):
    ip = get_ImageProcess(configPath)
    file_data = ip.selfieAnime(filePath)
    ip.save_file_content(filePath=output_path, fileData=file_data)
