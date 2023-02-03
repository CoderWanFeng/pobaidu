import toml

from pobaidu.lib.Const import DEFAULT_CONFIG_PATH_NAME


# def get_toml(toml_path):
#     """
#     解析配置文件
#     :param toml_path: 存放配置文件的位置和名称，在py文件的同级路径下
#     :return: 加载后的信息
#     """
#     try:
#         config_info = toml.load(toml_path)
#         print('配置文件【baidu-config.toml】读取成功')
#         return config_info
#     except:
#         print('配置文件【baidu-config.toml】读取失败，请查看视频，进行配置：https://www.bilibili.com/video/BV1Zv4y1r7zq')


def get_error_info(error_info):
    """
    检查接口返回数据是否错误
    :param error_info: 调用接口的返回数据
    :return:
    """
    error_url = 'http://python4office.cn/pobaidu/pobaidu-error/'
    if error_info.get('error_code', False):
        return f"接口调用错误，错误信息是{error_info}，原因和解决方法请查看官方文档：{error_url}"
    return False

