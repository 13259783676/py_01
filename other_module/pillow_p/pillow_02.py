#coding=utf-8
#description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/25'

from PIL import Image, ImageFilter

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('test.jpg')
assert isinstance(im,Image.Image)
# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg','jpeg')