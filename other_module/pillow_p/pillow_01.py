#coding=utf-8
#description：
from PIL import Image

_author_ = 'Kai,Chen'
_time_ = '2018/4/25'


#缩放图片
# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('test.jpg')
assert isinstance(im,Image.Image)
w, h = im.size
#获得图片尺寸
print('width:%s, height: %s'%(w, h))
# 缩放到50%:
im.thumbnail((w//2, h//2))
print('Resize image to: %s,%s' %(w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('thumbnail.jpg', 'jpeg')




