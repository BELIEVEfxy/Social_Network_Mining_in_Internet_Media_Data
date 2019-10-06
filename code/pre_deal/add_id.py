# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv

file_name=open('all_name_distinct.txt',encoding='UTF-8')
file_out=open('id_name.txt',mode='a',encoding='UTF-8')
line=file_name.readline()
cnt=1
while line:
    file_out.write(str(cnt)+','+line)
    line=file_name.readline()
    cnt+=1
print("ok")