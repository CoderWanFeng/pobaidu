import unittest

from pobaidu.core.ImageProcess import ImageProcess

from pobaidu.api.imageprocess import selfie_anime


class TestBaidu(unittest.TestCase):
    def test_selfie_anime(self):
        selfie_anime(img_path=r'file/img_cartoon.jpg')

    def test_colourize(self):
        ip = ImageProcess()
        res = ip.colourize(img_path=r'file/girl.jpg',output_path=r'./output/res.jpg')
        print(res)
