# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']
import numpy as np
import pandas as pd
import csv
from collections import Counter
#找出所有的边，分批写出
file_name=open('news_name2.txt',encoding='UTF-8')
file_out1=open('name_edge_1.txt',mode='a',encoding='UTF-8')
file_out2=open('name_edge_2.txt',mode='a',encoding='UTF-8')
file_out3=open('name_edge_3.txt',mode='a',encoding='UTF-8')
file_out4=open('name_edge_4.txt',mode='a',encoding='UTF-8')
file_out5=open('name_edge_5.txt',mode='a',encoding='UTF-8')
file_out6=open('name_edge_6.txt',mode='a',encoding='UTF-8')

line=file_name.readline()
cnt=1
big_list=[]
#每100000写入一个txt
while line:
    if cnt>100000:#写入第一个txt
        print(cnt)
        print("list: ", len(big_list))
        big_set=list(set(big_list))
        print("set: ", len(big_set))
        for j in range(0,len(big_list)):
            file_out1.write(big_list[j]+'\n')
        big_list.clear()
        big_set.clear()
        break
    if(cnt%10000==0):
        print(cnt)
        print("list: ", len(big_list))
        big_set=list(set(big_list))
        print("set: ", len(big_set))
        for j in range(0,len(big_list)):
            file_out1.write(big_list[j]+'\n')
        big_list.clear()
        big_set.clear()
    s=line[2:-3]
    arow=s.strip(',').split("', '")
    for i in range(0,len(arow)-1):
        for j in range(i+1,len(arow)):
            if arow[i]>arow[j]:
                temp=arow[i]
                arow[i]=arow[j]
                arow[j]=temp
            a_temp=arow[i]+','+arow[j]#little trick
            big_list.append(a_temp)

    line=file_name.readline()
    cnt+=1
file_out1.close()
#第2个txt
while line:
    if cnt>200000:#写入第一个txt
        print(cnt)
        print("list: ", len(big_list))
        big_set=list(set(big_list))
        print("set: ", len(big_set))
        for j in range(0,len(big_list)):
            file_out2.write(big_list[j]+'\n')
        big_list.clear()
        big_set.clear()
        break
    if(cnt%10000==0):
        print(cnt)
        print("list: ", len(big_list))
        big_set=list(set(big_list))
        print("set: ", len(big_set))
        for j in range(0,len(big_list)):
            file_out2.write(big_list[j]+'\n')
        big_list.clear()
        big_set.clear()
    s=line[2:-3]
    arow=s.strip(',').split("', '")
    for i in range(0,len(arow)-1):
        for j in range(i+1,len(arow)):
            if arow[i]>arow[j]:
                temp=arow[i]
                arow[i]=arow[j]
                arow[j]=temp
            a_temp=arow[i]+','+arow[j]#little trick
            big_list.append(a_temp)

    line=file_name.readline()
    cnt+=1
file_out2.close()
#第3个txt
while line:
    if cnt>300000:#写入第一个txt
        print(cnt)
        print("list: ", len(big_list))
        big_set=list(set(big_list))
        print("set: ", len(big_set))
        for j in range(0,len(big_list)):
            file_out3.write(big_list[j]+'\n')
        big_list.clear()
        big_set.clear()
        break
    if(cnt%10000==0):
        print(cnt)
        print("list: ", len(big_list))
        big_set=list(set(big_list))
        print("set: ", len(big_set))
        for j in range(0,len(big_list)):
            file_out3.write(big_list[j]+'\n')
        big_list.clear()
        big_set.clear()
    s=line[2:-3]
    arow=s.strip(',').split("', '")
    for i in range(0,len(arow)-1):
        for j in range(i+1,len(arow)):
            if arow[i]>arow[j]:
                temp=arow[i]
                arow[i]=arow[j]
                arow[j]=temp
            a_temp=arow[i]+','+arow[j]#little trick
            big_list.append(a_temp)

    line=file_name.readline()
    cnt+=1
file_out3.close()
#第4个txt
while line:
    if cnt>400000:#写入第一个txt
        print(cnt)
        print("list: ", len(big_list))
        big_set=list(set(big_list))
        print("set: ", len(big_set))
        for j in range(0,len(big_list)):
            file_out4.write(big_list[j]+'\n')
        big_list.clear()
        big_set.clear()
        break
    if(cnt%10000==0):
        print(cnt)
        print("list: ", len(big_list))
        big_set=list(set(big_list))
        print("set: ", len(big_set))
        for j in range(0,len(big_list)):
            file_out4.write(big_list[j]+'\n')
        big_list.clear()
        big_set.clear()
    s=line[2:-3]
    arow=s.strip(',').split("', '")
    for i in range(0,len(arow)-1):
        for j in range(i+1,len(arow)):
            if arow[i]>arow[j]:
                temp=arow[i]
                arow[i]=arow[j]
                arow[j]=temp
            a_temp=arow[i]+','+arow[j]#little trick
            big_list.append(a_temp)

    line=file_name.readline()
    cnt+=1
file_out4.close()
#第5个txt
while line:
    if cnt>500000:#写入第一个txt
        print(cnt)
        print("list: ", len(big_list))
        big_set=list(set(big_list))
        print("set: ", len(big_set))
        for j in range(0,len(big_list)):
            file_out5.write(big_list[j]+'\n')
        big_list.clear()
        big_set.clear()
        break
    if(cnt%10000==0):
        print(cnt)
        print("list: ", len(big_list))
        big_set=list(set(big_list))
        print("set: ", len(big_set))
        for j in range(0,len(big_list)):
            file_out5.write(big_list[j]+'\n')
        big_list.clear()
        big_set.clear()
    s=line[2:-3]
    arow=s.strip(',').split("', '")
    for i in range(0,len(arow)-1):
        for j in range(i+1,len(arow)):
            if arow[i]>arow[j]:
                temp=arow[i]
                arow[i]=arow[j]
                arow[j]=temp
            a_temp=arow[i]+','+arow[j]#little trick
            big_list.append(a_temp)

    line=file_name.readline()
    cnt+=1
file_out5.close()
#第6个txt
while line:
    if(cnt%10000==0):
        print(cnt)
        print("list: ", len(big_list))
        big_set=list(set(big_list))
        print("set: ", len(big_set))
        for j in range(0,len(big_list)):
            file_out6.write(big_list[j]+'\n')
        big_list.clear()
        big_set.clear()
    s=line[2:-3]
    arow=s.strip(',').split("', '")
    for i in range(0,len(arow)-1):
        for j in range(i+1,len(arow)):
            if arow[i]>arow[j]:
                temp=arow[i]
                arow[i]=arow[j]
                arow[j]=temp
            a_temp=arow[i]+','+arow[j]#little trick
            big_list.append(a_temp)

    line=file_name.readline()
    cnt+=1
#结尾处理
print("list: ", len(big_list))
big_set=list(set(big_list))
print("set: ", len(big_set))
for j in range(0,len(big_list)):
    file_out6.write(big_list[j]+'\n')
big_list.clear()
big_set.clear()
print("finish!")