
import urllib
from datetime import datetime
from urllib import request
from urllib.request import Request

import os

from bs4 import BeautifulSoup

def saveImage(urls,output_url):
    if urls is None:
        return
    if not os.path.exists(output_url):
        os.makedirs(output_url)
    for url in  urls:
        image_url=url['src']

        file_name=os.path.join(output_url,os.path.basename(image_url))
        print("%s to %s" % (image_url,file_name))
        urllib.request.urlretrieve(image_url,file_name )

def download(url):
    if url is None:
        return
    req=Request(url)
    content=request.urlopen(req).read()
    return content.decode("utf-8",'ignore')
def parser(content):
    if content is None:
        return
    soup=BeautifulSoup(content,'html.parser')
    urls=soup.find_all('img',class_='BDE_Image')
    return urls

if __name__=='__main__':

    root_url='https://tieba.baidu.com/p/5224471861?pn='
    output_url=os.getcwd()+os.path.sep+'images'
    max_page=3;#最大页数
    try:
        time1=datetime.now()
        for p in range(max_page):
            url=os.path.join(root_url,str(p))
            content = download(url)
            urls = parser(content)
            saveImage(urls, output_url)
        time2=datetime.now()
        print('耗时：%s 秒' % (time2-time1).seconds)
    except Exception as e:
        print(e)