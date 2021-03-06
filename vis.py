
#!usr/bin/env python
#encoding:utf-8
from __future__ import division
from generate_mat import *
'''
功能： 词云的可视化模块
'''
from cv2 import imread
import os
import sys
import json
import numpy as np
from PIL import Image
from matplotlib import colors
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
 
#自定义颜色列表
color_list=['#CD853F','#DC143C','#00FF7F','#FF6347','#8B008B','#00FFFF','#0000FF','#8B0000','#FF8C00',
            '#1E90FF','#00FF00','#FFD700','#008080','#008B8B','#8A2BE2','#228B22','#FA8072','#808080']
 
 
 
def simpleWC1(sep=' ',back='black',freDictpath='data_fre.json',savepath='res.png'):
    '''
    词云可视化Demo
    '''
    try:
        with open(freDictpath) as f:
            data=f.readlines()
            data_list=[one.strip().split(sep) for one in data if one]
        fre_dict={}
        for one_list in data_list:
            fre_dict[unicode(one_list[0])]=int(one_list[1])
    except:
        fre_dict=freDictpath
    wc=WordCloud(font_path='font/simhei.ttf',#设置字体  #simhei
                background_color=back, #背景颜色
                max_words=1300,# 词云显示的最大词数
                max_font_size=120, #字体最大值
                margin=3,  #词云图边距
                width=1800,  #词云图宽度
                height=800,  #词云图高度
                random_state=42)
    wc.generate_from_frequencies(fre_dict)  #从词频字典生成词云
    plt.figure()  
    plt.imshow(wc)
    plt.axis("off")
    wc.to_file(savepath)
 
 
def simpleWC2(sep=' ',back='black',backPic='a.png',freDictpath='data_fre.json',savepath='res.png'):
    '''
    词云可视化Demo【使用背景图片】
    '''
    try:
        with open(freDictpath) as f:
            data=f.readlines()
            data_list=[one.strip().split(sep) for one in data if one]
        fre_dict={}
        for one_list in data_list:
            fre_dict[unicode(one_list[0])]=int(one_list[1])
    except:
        fre_dict=freDictpath
    back_coloring=imread(backPic)
    wc=WordCloud(font_path='simhei.ttf',#设置字体  #simhei
                background_color=back,max_words=1300,
                mask=back_coloring,#设置背景图片
                max_font_size=80, #字体最大值
                margin=3,width=1600*15,height=900*15,random_state=42,
                prefer_horizontal = 0.9,
                scale= 30)
    wc.generate_from_frequencies(fre_dict)  #从词频字典生成词云
    wc.to_file(savepath)
 
 
def simpleWC3(sep=' ',back='black',freDictpath='data_fre.json',savepath='res.png'):
    '''
    词云可视化Demo【自定义字体的颜色】
    '''
    #基于自定义颜色表构建colormap对象
    colormap=colors.ListedColormap(color_list)  
    try:
        with open(freDictpath) as f:
            data=f.readlines()
            data_list=[one.strip().split(sep) for one in data if one]
        fre_dict={}
        for one_list in data_list:
            fre_dict[unicode(one_list[0])]=int(one_list[1])
    except:
        fre_dict=freDictpath
    wc=WordCloud(font_path='font/simhei.ttf',#设置字体  #simhei
                background_color=back,  #背景颜色
                max_words=1300,  #词云显示的最大词数
                max_font_size=120,  #字体最大值
                colormap=colormap,  #自定义构建colormap对象
                margin=2,width=1800,height=800,random_state=42,
                prefer_horizontal=0.5)  #无法水平放置就垂直放置
    wc.generate_from_frequencies(fre_dict)
    plt.figure()  
    plt.imshow(wc)
    plt.axis("off")
    wc.to_file(savepath)

if __name__ == "__main__":
    simpleWC2(sep=' ',back='white',backPic='backPic/C.png',freDictpath=f,savepath='simpleWC2.png')

