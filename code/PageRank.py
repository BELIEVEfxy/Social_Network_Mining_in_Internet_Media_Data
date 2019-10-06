# -*- coding: UTF-8 -*-
import csv
import os
import numpy as np 
import pandas as pd
import networkx as nx

# filename = 'id1-id2-noweight-1118.txt'
# G=nx.Graph()

# cnt=1
# with open(filename) as file:
#     for line in file:
#         if cnt%100000==0:
#             print(cnt)
#         cnt+=1
#         head,tail = [int(x) for x in line.split('\t')]
#         G.add_edge(head,tail)
# print("read finish")
# pr=nx.pagerank(G,alpha=0.85)
# print("calculate finish")
# file_out=open("pagerank.csv",mode='a',encoding='UTF-8')
# dict_page={}
# list_node=[]
# for node, pageRankValue in pr.items():
#     list_node.append(node)
#     #file_out.write(str(node)+','+str(pageRankValue)+'\n')
#     dict_page[node]=pageRankValue
# for i in range(1,80189):
#     if i in list_node:
#         file_out.write(str(node)+','+str(pageRankValue)+'\n')
#     else:
#         file_out.write(str(node)+','+'-1'+'\n')
# print("write finish")

file_in=open('pagerank.txt',encoding='UTF-8')
line=file_in.readline()
list_node=[]
dict_page={}
cnt=1
while line:
    if cnt%10000==0:
        print(cnt)
    cnt+=1
    line=line.strip().split(',')
    line[0]=int(line[0])
    line[1]=float(line[1])
    list_node.append(line[0])
    dict_page[line[0]]=line[1]
    line=file_in.readline()
print("read finish")
# dict_page=sorted(dict_page.items(),key = lambda x:x[0],reverse = False)
# print("sort finish")
file_out=open('pa.csv',mode='w',encoding='UTF-8')
# dictp={}
# for i in range(0,len(dict_page)):
#     dictp[dict_page[i][0]]=dict_page[i][1]
#     #file_out.write(dict_page[i][0]+','+str(dict_page[i][1])+'\n') 
print(len(list_node))
for i in range(1,80189):
    if i %100==0:
        print(i)
    if i in list_node:
        #print(i)
        file_out.write(str(i)+','+str(dict_page[i])+'\n')
    else:
        file_out.write(str(i)+','+'-1'+'\n')
print("write finish!")