from os import times
import random, string, time
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

# 发送邮箱验证码
from smtplib import SMTP_SSL, SMTP
from email.mime.text import MIMEText
from email.header import Header

# 发送QQ邮箱验证码， 参数为收件箱地址和随机生成的验证码
def send_email(receiver, ecode):
    sender = 'Nebula <1057324546@qq.com>'  # 邮箱地址和发件人签名
    # 定义发送邮件的内容， 支持HTML标签和CSS样式
    content = f"<br/>欢迎来到NEBULA的世界，这里有浩瀚的星辰和美好的心灵，您的邮箱验证码是：<span style = 'color: red; font-size: 20px;'>{ecode}</span> ，请复制到注册窗口进行验证，开启你的星际之旅！"
    # 实例化邮件对象， 并指定邮件的关键信息
    message = MIMEText(content, 'html', 'utf-8')
    # 指定邮件的标题， 同样使用utf-8编码
    message['Subject'] = Header('欢迎注册Nebula，请收好您的注册验证码', 'utf-8')
    message['From'] = sender        # 指定发件人信息
    message['To'] = receiver        # 指定收件人邮箱地址

    smtpObj = SMTP_SSL('smtp.qq.com')       # 建议与QQ邮件服务器的连接
    # smtpObj = SMTP('smtp.qq.com')       # 不是 SSL 方式连接的邮箱
    # 通过你的邮箱账号和获取到的授权码登录QQ邮箱
    smtpObj.login(user='1057324546@qq.com', password='dkjjmqheyetebedd')      # 密码不正确需调整
    # 指定发件人，收件人和邮件内容
    smtpObj.sendmail(sender, receiver, str(message))
    smtpObj.quit()

# 生成6为随机字符串作为邮箱验证码
def gen_email_code():
    str = random.sample(string.ascii_letters + string.digits, 6)
    return ''.join(str)

# code = gen_email_code()
# print(code)
# send_email('papillon-nebula@outlook.com', code)


# 压缩图片， 通过参数 width 指定压缩后的图片大小
def compress_image(source, dest, width):
    from PIL import Image
    # 如果图片宽度大于1200， 则调整为1200的宽
    im = Image.open(source)
    x, y = im.size
    if x > width:
        # 等比缩放
        ys = int(y * width / x)
        xs = width
        # 调整当前图片的尺寸（同时也会压缩大小）
        temp = im.resize((xs, ys), Image.ANTIALIAS)
        # 将图片保存并使用80%的质量进行压缩
        temp.save(dest, quality=80)
    # 如果尺寸小于指定宽度则不缩减尺寸，只压缩保存
    else:
        im.save(dest, quality=80)


# 解析文章内容中的图片地址
def parse_image_url(content):
    import re
    temp_list = re.findall('<img src="(.+?)"', content)     # 非贪婪模式下的正则表达式（贪婪：按照最大（长）值进行匹配）
    url_list = []
    for url in temp_list:
        # 如果图片类型为 gif ， 则直接跳过， 不对其进行处理
        if url.lower().endswith('.gif'):
            continue
        url_list.append(url)
    return url_list

# 远程下载指定URL地址的图片，并保存到临时目录中
def download_image(url, dest):
    import requests
    response = requests.get(url)
    with open(file=dest, mode='wb') as file:
        file.write(response.content)

# 解析列表中的图片URL地址并生成缩略图，返回缩略图名称
def generate_thumb(url_list):
    # 根据URL 地址解析初期文件名和域名
    # 通常建议使用文章内容中的第一张土拍你来生成缩略图
    # 先遍历 url_list，查找里面是否存在本地上传图片，找到及处理，代码运行结束
    for url in url_list:
        if url.startswith('/upload/'):
            filename = url.split('/')[-1]
            # 找到本地图片后对其进行压缩处理，设置缩略图宽度为400像素即可
            compress_image('./resource/upload/' + filename,
                            './resource/thumb/' + filename, 400)
            return filename

    # 如果在内容中没有找到本地图片，则需要先将王略图片下载到本地再处理
    # 直接将第一张图片作为缩略图， 并生成基于时间戳的标准文件名
    url = url_list[0]
    filename = url.split('/')[-1]
    suffix = filename.split('.')[-1]
    thumbname = times.strftime('%Y%m%d_%H%M%S.' + suffix)
    download_image(url, './resource/download/' + thumbname)
    compress_image('./resource/download/' + thumbname, './resource/thumb/' + thumbname, 400)

    return thumbname        # 返回当前缩略图的文件名

# url = 'https://spyre-theme.bitbucket.io/v1.4.0/assets/img/backgrounds/bg-10.jpg'