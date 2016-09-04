#!/usr/bin/python
#encoding:utf-8
__author__ = 'harbour'
import os
from PIL import Image
from knn import knn
url=r"C:\Users\byharbour\Desktop\AutoPostingMarching\pic_test"

# 当前项目有两个文件，image_deal为图片处理，knn为分类。
#读取的是一本地存放待识别图片的文件目录url，image_deal处理之后传给
#knn.py文件，然后返回一个字符串类型的识别的字符 "xxxx.png" ，切将识别之后的图片以识别之后
#的名称命名并保存在本地result文件当中。
def image_deal(f):
    filepath = os.path.join(url, f)
    im=Image.open(filepath)
    im=im.convert("L")
    pixdata=im.load()
    width=im.size[0]
    height=im.size[1]

    #二值化
    for i in range(width):
        for j in range(height):
            if pixdata[i,j]<123:
                pixdata[i,j]=0
            else:
                pixdata[i,j]=255
    crop_array=[]
    for i in xrange(width):
            black=0
            for j in xrange(height):
                if pixdata[i,j]==0:
                    black+=1
            if black>=3:
                crop_array.append(1)
            else:
                crop_array.append(0)
    crop_end=0
    crop_start=0
    flag=0
    cnt=0
    count=0
    result=r"./result/"
    #单个字符分割出来
    for i in range(width-1):
        mark=0
        if cnt==4:
            break
        if crop_array[i]==0 and crop_array[i+1]==1:
            crop_start=i
        if crop_array[i]==1 and crop_array[i+1]==0:
            crop_end=i
            mark=1
        # if cnt==3 and mark==0:
        #     crop_start=i
        #     crop_end=width
        #     flag=1
        if(crop_end>crop_start):
            flag=1
        if flag==1:
            region=(crop_start,0,crop_end,height)
            crop_image=im.crop(region)
            crop_image=crop_image.resize((32,32))
            flag=0
            crop_start=0
            crop_end=0
            cnt+=1
            #转换成字符图写入文件
            logfile=open(str(cnt) +'.txt','w')
            for i in range(32):
                for j in range(32):
                    if crop_image.getpixel((j,i))==255:
                        logfile.write('0')
                    else:
                        logfile.write('1')
                logfile.write('\n')
            logfile.close()
            num=knn(str(cnt)+'.txt')
            result+=num
    result+=".png"
    print result
    im.save(result);



def start_recognize(url):
    for imgfile in os.listdir(url):
        if imgfile.endswith(".png"):
            image_deal(imgfile)

# if __name__=='__main__':
#     start_recognize(url)