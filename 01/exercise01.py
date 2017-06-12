'''
在图像右上角添加数字
'''
import os

from PIL import Image,ImageDraw,ImageFont,ImageColor
def add_num(inputPath,number,outputPath):
    image = Image.open(inputPath, "r")
    draw=ImageDraw.Draw(image)
    font=ImageFont.truetype("ARCENA.ttf", size=24)
    fillcolor=ImageColor.getrgb("rgb(255,0,0)")
    width,height=image.size
    draw.text((width-48,12),number,font=font,fill=fillcolor)
    image.save(outputPath,'jpeg')
    return 0;
if __name__=='__main__':
    path=os.getcwd()+os.path.sep
    inputPath=path+"input.png"
    outputPath=path+"output.jpg"
    add_num(inputPath,"666",outputPath)