# -*- coding: UTF-8 -*-
'''
@Author  ：程序员晚枫，B站/抖音/微博/小红书/公众号
@WeChat     ：CoderWanFeng
@Blog      ：www.python-office.com
@Date    ：2023/1/22 15:23
@Description     ：
'''

from pobaidu.core.ImageProcess import ImageProcess
import requests


def get_ImageProcess(configPath):
    ip = ImageProcess()
    ip.set_config(configPath)
    return ip


def colourize(img_path, output_path=r'./', configPath=None):
    """
    黑白照片上色
    :param img_path:
    :param output_path:
    :param configPath:
    :return:
    """
    ip = get_ImageProcess(configPath)
    file_data = ip.colourize(img_path)
    ip.save_file_content(filePath=output_path, fileData=file_data)


def selfieAnime(filePath, output_path=r'./', configPath=None):
    ip = get_ImageProcess(configPath)
    file_data = ip.selfieAnime(filePath)
    ip.save_file_content(filePath=output_path, fileData=file_data)


# def face_merge():
#     '''
#     人脸融合
#     '''
#
#     request_url = "https://aip.baidubce.com/rest/2.0/face/v1/merge"
#
#     params = "{\"image_template\":{\"image\":\"sfasq35sadvsvqwr5q...\",\"image_type\":\"BASE64\",\"quality_control\":\"NONE\"},\"image_target\":{\"image\":\"sfasq35sadvsvqwr5q...\",\"image_type\":\"BASE64\",\"quality_control\":\"NONE\"}}"
#     access_token = '[调用鉴权接口获取的token]'
#     request_url = request_url + "?access_token=" + access_token
#     headers = {'content-type': 'application/json'}
#     response = requests.post(request_url, data=params, headers=headers)
#     if response:
#         print(response.json())
