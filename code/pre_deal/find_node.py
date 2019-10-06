# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']
import numpy as np
import pandas as pd
import csv
#找出所有的点，利用set去重
#读1000条写出一次
file_name=open('news_name2.txt',encoding='UTF-8')
file_out=open('name_list2.txt',mode='a',encoding='UTF-8')
line=file_name.readline()
name_set=set()
cnt=1
while line:
    if(cnt%1000==0):
        print(cnt)
    s=line[2:-3]
    arow=s.strip(',').split("', '")
    #print(arow)
    for i in range(0,len(arow)):
        name_set.add(arow[i])
    line=file_name.readline()
    cnt+=1
#结尾处理
name_list=list(name_set)
for j in range(0,len(name_list)):
    file_out.write(name_list[j]+'\n')
print("write finish!")

