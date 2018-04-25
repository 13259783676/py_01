#coding=utf-8
#description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/25'

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

def randomChar():
    return chr(random.randint(65, 90))

t = randomChar()

print(dir(ImageFont.sys()))

