import unittest

from pobaidu.api.face import face_merge

from pobaidu.core.ImageProcess import ImageProcess

from pobaidu.api.imageprocess import selfieAnime, colourize


class TestBaidu(unittest.TestCase):
    def test_selfie_anime(self):
        selfieAnime(filePath=r'file/img_cartoon.jpg')

    def test_colourize(self):
        res = colourize(img_path=r'file/girl.jpg', output_path=r'./output/res.jpg')
        print(res)

    def test_face_merge(self):
        face_merge(base_img_path=r'C:\Users\Lenovo\Desktop\temp\刘德华.jpg',
                   face_img_path=r'C:\Users\Lenovo\Desktop\temp\6606c755dd77427fb06e2e36eef969f2.png')
