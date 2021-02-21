import random, string
from typing import Sized, Text
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO


class ImageCode():
    # 生成用于绘制字符串的随机颜色
    def rand_color(self):
        red = random.randint(32, 255)
        green = random.randint(0,127)
        blue = random.randint(0,255)
        return red, green, blue
    # 生成4为随机字符串
    def gen_text(self):
        # sample 用于从一个大的列表或字符串中，随机选取 N 个字符，来构建出一个子列表
        list = random.sample(string.ascii_letters+string.digits, 4)
        print(list)         # 构建出的列表
        print(''.join(list))    # 变为字符串   
        return ''.join(list)
    # 画一些干扰线，其中 draw 为 PIL 中的 ImageDraw 对象
    def draw_lines(self, draw, num, width, height):
        for num in range(num):
            x1 = random.randint(0, width / 2)
            y1 = random.randint(0, height / 2)
            x2 = random.randint(0, width)
            y2 = random.randint(0, height)
            draw.line(((x1,y1), (x2,y2)), fill = 'black', width = 2)
    # 绘制验证码图片
    def draw_verify_code(self):
        code = self.gen_text()
        width, height = 120, 50     # 设定图片大小， 可根据实际需求调整
        # 创建图片对象， 并设定背景色为白色
        im = Image.new('RGB', (width, height), 'white')
        # 选择使用何种字体及字体大小
        font = ImageFont.truetype(font='arial.ttf', size = 40)
        draw = ImageDraw.Draw(im)       # 新建 ImageDraw 对象
        # 绘制字符串
        for i in range(4):
            draw.text((5 + random.randint(-3, 3) + 23 * i, 5 + random.randint(-3, 3)),
                    text = code[i], fill = self.rand_color(), font=font)
        # 绘制干扰线
        self.draw_lines(draw, 2, width, height)
        im.show()       # 如需临时调试， 可直接将生成的图片显示出来
        return im, code

# ImageCode().gen_text()
# ImageCode().draw_verify_code()

    # 生成图片验证码并返回给控制器
    def get_code(self):
        image, code = self.draw_verify_code()
        buf = BytesIO()
        image.save(buf, 'jpeg')
        bstring = buf.getvalue()
        return code, bstring