# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 14:57:18 2018

@author: zha200
"""
import pandas as pd

#1. read segmented data stored in txt file 

fileName = 'B0005.txt'
#data = pd.read_csv(fileName, sep = ",", skiprows=range(0,5))
data = pd.read_table(fileName, sep=',', comment='#')
 
#1. normalize the q and v columns
# for V columns, normalize w.r.t Vn = 3.2V
# for Q columns, change sign and normalize w.r.t   6600 (determined using idxmax)

data1 = data.iloc[:,1:11].apply(lambda x: x/3.2)
data2 = data.iloc[:,11:21].apply(lambda x: -x/6600)
data1 = data1.reset_index(drop=True)
data2 = data2.reset_index(drop=True)
data3 = pd.concat([data1, data2], axis=1)
#data[:,11:21].apply(lambda x: -x/6600)                   
#list(data)
