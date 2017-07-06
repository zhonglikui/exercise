#http://blog.csdn.net/liuzhixiong_521/article/details/51881719
import os

import sys


def get_files(path):
    filePath=os.listdir(path)
    files=[]
    for f in filePath:
        file=os.path.join(path,f)
        if os.path.isfile(file):
            files.append(file)
            print('%s is file'% file)
        elif os.path.isdir(file):
            files+=get_files(file)
            print(('%s is dir'% file))
    return files
def count_line(files):
    line,blank,note=0,0,0
    for file in files:
        f=open(file,'rb')
        for l in f:
            line+=1
        f.close()
    return line,blank,note
if __name__=="__main__":
     inputPath=os.path.abspath(os.path.join(sys.path[0],os.pardir,os.pardir))
     files=get_files(inputPath)
     lines=count_line(files)
     print('共有%s行，空白有%s行，注释%s行'%(lines[0],lines[1],lines[2]))