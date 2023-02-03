import base64
import json

import requests
from aip import AipImageProcess

from pobaidu.lib.Config import poaiConfig

from pobaidu.lib.CommonUtils import get_error_info


class Face(poaiConfig):
    def __init__(self):
        self.BAIDU_AI_CFG = None
        self.CLIENT_API = None
        self.CLIENT_SECRET = None
        self.CLIENT_ID = None
        self.CLIENT = None

    def set_config(self, configPath):
        self.BAIDU_AI_CFG = self.get_config(configPath)
        if self.BAIDU_AI_CFG['baidu-ai']['client_secret'] and self.BAIDU_AI_CFG['baidu-ai']['client_id']:
            self.CLIENT_SECRET = self.BAIDU_AI_CFG['baidu-ai']['client_secret']
            self.CLIENT_ID = self.BAIDU_AI_CFG['baidu-ai']['client_id']

    def get_access_token(self):
        url = f"https://aip.baidubce.com/oauth/2.0/token?client_id={self.CLIENT_ID}&client_secret={self.CLIENT_SECRET}&grant_type=client_credentials"
        payload = ""
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        token_response = requests.request("POST", url, headers=headers, data=payload)
        res = json.loads(token_response.text)
        return res['access_token']

    def get_file_content(self, filePath):
        """
        读取图片
        :param filePath: 读取图片
        :return:
        """
        with open(filePath, 'rb') as fp:
            return fp.read()

    def save_file_content(self, filePath, fileData):
        """
        将图片保存为文件
        :param filePath: 输出位置
        :param fileData: 图片数据，base64格式
        :return:
        """
        if get_error_info(fileData):
            print(get_error_info(fileData))
        else:
            # 解码图片
            imgdata = base64.b64decode(fileData['image'])
            # 将图片保存为文件
            with open(filePath, 'wb') as f:
                f.write(imgdata)

    def selfieAnime(self, filePath):
        """
        人像动漫化
        :param filePath:
        :return:
        """
        file_content = self.get_file_content(filePath)
        res_image = self.CLIENT.selfieAnime(file_content)
        return res_image

    def colourize(self, filePath):
        '''
        给黑白图片上色 https://ai.baidu.com/ai-doc/IMAGEPROCESS/Bk3bclns3
        :param img_path: 黑白图片的位置
        :param output_path: 上色后图片的保存位置
        :return:
                {
                    "log_id": "6876747463538438254",
                    "image": "处理后图片的Base64编码"
                }
        '''
        file_content = self.get_file_content(filePath)
        res_image = self.CLIENT.colourize(file_content)
        return res_image
