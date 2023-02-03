# -*- coding: UTF-8 -*-
'''
@Author  ：程序员晚枫，B站/抖音/微博/小红书/公众号
@WeChat     ：CoderWanFeng
@Blog      ：www.python-office.com
@Date    ：2023/2/3 21:49 
@Description     ：
'''
import base64

from pobaidu.lib.CommonUtils import get_error_info


def get_img_base64(img_path):
    with open(img_path, 'rb') as fp:
        img_base64 = base64.b64encode(fp.read()).decode()
        return img_base64
    return None


