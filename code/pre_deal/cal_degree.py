# -*- coding: UTF-8 -*-
#计算每个结点的度
import csv
import os

file_in_1=open("id1_id2_weight_1.csv",encoding='UTF-8-sig')
file_in_2=open("id1_id2_weight_2.csv",encoding='UTF-8-sig')
file_in_3=open("id1_id2_weight_3.csv",encoding='UTF-8-sig')
file_degree=open("degree.txt",mode='a',encoding='UTF-8')

dict_neibor={}
#initial
for i in range(1,361643):
    dict_neibor[i]=0

line1=file_in_1.readline()
cnt=1
while line1:
    if cnt%100000==0:
        print(cnt)
    cnt+=1
    line1=line1.strip().split(',')
    #print(line1)
    line1[0]=int(line1[0])
    line1[1]=int(line1[1])
    dict_neibor[line1[0]]+=1
    dict_neibor[line1[1]]+=1
    line1=file_in_1.readline()
file_in_1.close()
print("1 finish")
line2=file_in_2.readline()
while line2:
    if cnt%100000==0:
        print(cnt)
    cnt+=1
    line2=line2.strip().split(',')
    line2[0]=int(line2[0])
    line2[1]=int(line2[1])
    dict_neibor[line2[0]]+=1
    dict_neibor[line2[1]]+=1
    line2=file_in_2.readline()
file_in_2.close()
print("2 finish")
line3=file_in_3.readline()
while line3:
    if cnt%100000==0:
        print(cnt)
    cnt+=1
    line3=line3.strip().split(',')
    line3[0]=int(line3[0])
    line3[1]=int(line3[1])
    dict_neibor[line3[0]]+=1
    dict_neibor[line3[1]]+=1
    line3=file_in_3.readline()
file_in_3.close()
print("3 finish")
for i in range(1,361643):
    file_degree.write(str(i)+','+str(dict_neibor[i])+'\n')
print("write finish")