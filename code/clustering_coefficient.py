# -*- coding: UTF-8 -*-
import csv
import os

file_in=open("id1_id2_no_weight.csv",encoding='UTF-8')
file_out=open("clustering_coefficient.csv",mode='a',encoding='UTF-8')
file_out1=open("triangle.csv",mode='a',encoding='UTF-8')
dict_set={}
dict_juji={}
#initial
for i in range(1,361643):
    temp=set()
    dict_set[i]=temp
    dict_juji[i]=0
for j in range(361542,361643):
    print(dict_juji[i])
#edge=[]
#寻找每个结点的邻居，并压入集合中
line=file_in.readline()
cnt=1
while line:
    if cnt%100000==0:
        print(cnt)
    cnt+=1
    line=line.strip().split(',')
    line[0]=int(line[0])
    line[1]=int(line[1])
    #edge.append(temp)
    dict_set[line[0]].add(line[1])
    dict_set[line[1]].add(line[0])
    line=file_in.readline()
print("read set finish!")
file_in.close()
#计算两个顶点集合的交集，然后更新每个节点所在三角形的个数
file_in=open("id1_id2_no_weight.csv",encoding='UTF-8')
line1=file_in.readline()
cnt=1
while line1:
    if cnt%100000==0:
        print(cnt)
    cnt+=1
    line1=line1.strip().split(',')
    u=line1[0]=int(line1[0])
    v=line1[1]=int(line1[1])
    num=(len(dict_set[u]&dict_set[v]))
    dict_juji[u]+=num
    dict_juji[v]+=num
    line1=file_in.readline()
print(dict_juji[361642])
for i in range(1,361643):
    file_out1.write(str(i)+','+str(dict_juji[i])+'\n')
print(i)
print("write finish")
#计算聚集系数
file_in=open("degree.txt",encoding='UTF-8')
line=file_in.readline()
while line:
    line=line.strip().split(',')
    index=line[0]=int(line[0])
    degree=line[1]=int(line[1])
    if degree==0 or degree==1:
        dict_juji[index]=-1
        continue
    dict_juji[index]=dict_juji[index]/(degree*(degree-1))
    line=file_in.readline()
    file_out.write(str(index)+','+str(dict_juji[index])+'\n')
print("write finish")