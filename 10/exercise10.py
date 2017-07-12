import random
import string

from PIL import Image, ImageFont, ImageDraw, ImageFilter


def getRandomChar():
    poolOfchars=string.ascii_letters+string.digits
    code=''.join([random.choice(poolOfchars) for i in range(4)])
    return code
def getColor():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
def getCodePicture(char,color):
    width = 240
    height = 60
    # 创建画布
    image = Image.new('RGB', (width, height), (180,180,180))
    #字体
    font = ImageFont.truetype('ARCENA.ttf', 50)
    draw = ImageDraw.Draw(image)
    #把字符绘制到图片上
    for t in range(len(char)):
        draw.text((60*t+10,5),char[t],font=font,fill=color)
    #填充噪点
    for p in range(random.randint(1000,2000)):
        draw.point((random.randint(0,width),random.randint(0,height)),fill=getColor())
    #模糊处理
    image=image.filter(ImageFilter.BLUR)
    #保存图片
    image.save(str(char)+".jpg",'JPEG')


if __name__=='__main__':
    chars=getRandomChar()
    color=getColor()
    getCodePicture(chars,color)