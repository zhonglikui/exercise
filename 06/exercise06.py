import os

from PIL import Image

if __name__=="__main__":
     inputPath=os.getcwd()+os.path.sep+'input'
     outputPath = os.getcwd() + os.path.sep + 'output'+os.path.sep

     for i in os.listdir(inputPath):
         # 检查后缀
         postfix = os.path.splitext(i)
         print(postfix[0],':',postfix[1])
         if postfix[1]==".jpg" or postfix[1]==".png":
             im=Image.open(inputPath+os.path.sep+i)
             width=im.size[0]
             height=im.size[1]
             max_width=720
             max_height=1280
             scaleX = width / max_width;
             scaleY = height / max_height;
             scale = 1;
             if scaleX>scaleY :
                 scale=scaleX
             elif scaleY>scaleX :
                 scale=scaleY


             real_width=width/scale
             real_height=height/scale
             print(width,height,scaleX,scaleY,scale,real_width,real_height)
             size=real_width,real_height
             im.thumbnail(size)
             if not os.path.exists(outputPath):
                 os.makedirs(outputPath)
             im.save(outputPath+postfix[0]+".jpg","JPEG")

             #  im = Image.open(filesource + name)
             # 缩放比例
             #rate = max(im.size[0] / 640.0 if im.size[0] > 640 else 0, im.size[1] / 1136.0 if im.size[1] > 1136 else 0)
            # if rate:
             #    im.thumbnail((im.size[0] / rate, im.size[1] / rate))
            # im.save(destsource + name, imgtype)
