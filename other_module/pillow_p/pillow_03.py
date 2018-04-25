# coding=utf-8
# description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/25'

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


# 随机字母:
def randomChar():
    return chr(random.randint(65, 90))


# 随机颜色1:
def randomColor1():
    return (random.randint(60, 255), random.randint(60, 255), random.randint(60, 255))


# 随机颜色2:
def randomColor2():
    # return (random.randint(60, 255), random.randint(60, 255), random.randint(60, 255))
    return (0, 0, 0)


# 240x60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
assert isinstance(image, Image.Image)

# 创建Font对象:
font = ImageFont.truetype('Lazara.ttf', 36)
# 创建draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=randomColor1())
# 输出文字
for t in range(4):
    draw.text((60 * t + 10, 10), randomChar(), font=font, fill=randomColor2())
# 模糊滤镜
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
