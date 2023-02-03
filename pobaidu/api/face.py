# -*- coding: UTF-8 -*-
'''
@Author  ：程序员晚枫，B站/抖音/微博/小红书/公众号
@WeChat     ：CoderWanFeng
@Blog      ：www.python-office.com
@Date    ：2023/2/2 23:39 
@Description     ：
'''

import base64

import requests
import json

from pobaidu.core.Face import Face
from pobaidu.lib.Const import FACE_URL
from pobaidu.lib.FileUtils import get_img_base64


def get_Face(configPath):
    face_instance = Face()
    face_instance.set_config(configPath)
    return face_instance


def face_merge(base_img_path='', face_img_path='', output_path=r'./output/face_merge.jpg', configPath=None):
    face_instance = get_Face(configPath)
    url = FACE_URL + face_instance.get_access_token()
    base_img = get_img_base64(base_img_path)
    face_img = get_img_base64(face_img_path)
    payload = json.dumps({
        "image_target": {
            "image": face_img,
            "image_type": "BASE64",
            "quality_control": "NONE"
        },
        "image_template": {
            "image": base_img,
            "image_type": "BASE64"
        },
        "merge_degree": "COMPLETE"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # print(json.loads(response.text)['result']['merge_image'])
    res_img = json.loads(response.text)['result']['merge_image']
    # 解码图片
    imgdata = base64.b64decode(res_img)
    # print(imgdata)
    # save_file_content(filePath=output_path, fileData=imgdata)
    # # 将图片保存为文件
    with open(output_path, 'wb') as f:
        f.write(imgdata)
