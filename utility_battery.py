# -*- coding: utf-8 -*-
"""
Created on Fri May  4 10:26:02 2018

@author: zha200
"""

#import math as mth
#import sys
import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
#import pandas as pd


class MatFileLoader:
# The class MatFileLoader is designed to exctract information from the mat file containing the battery test data from NASA. 
# The mat file is a multilayer structure as described by the annotation below (level 0 to level 3); 
# mat file data strucutre
# level 0: fileName'B0005' matfile is a 1X1 struct
# level 1: 'cylce' is a 1 field struct the value of which is a 1X616 array of struct
# level 2:   a array of 616 struct, each struct element has 4 field defined as ['type','ambient T','time','data'. 'data' is 1X1 array of struct
# level 3:  'data'  struct have 6 fields listed below:
        # 'Voltage_measured','Current_measured','Temperature_measured','Current_charge','Voltage_charge','Time'
#        each struct will be loaded into a 1X1 ndarray first, so need to unpack first
    def __init__(self, fileName):
        self.matData = sio.loadmat(fileName+'.mat')[fileName] # load mat file data into a dic and search for value
        
    def get_data(self, cycleNum, dataName):
#       cycle number: the index of cycles to extact(level 2)
#       dataName: the name of data (Level 3)
       try:
           return np.squeeze(self.matData['cycle'][0,0][0,cycleNum]['data'][0,0][dataName])
       except:
           print('MatFileLoader-get_data: Wrong value for data column name')
           
    def get_type(self, cycleNum):
        return np.squeeze(self.matData['cycle'][0,0][0,cycleNum]['type'])
    def get_time(self, cycleNum):
        return np.squeeze(self.matData['cycle'][0,0][0,cycleNum]['time'])
    def get_ambient_temperature(self, cycleNum):
        return np.squeeze(self.matData['cycle'][0,0][0,cycleNum]['ambient_temperature'])
    def plot_data(self,cycleNum, dataNameList):
# visulisation of data specified by List: dataNameList 
        fig1 = plt.figure()
        fig1.add_subplot(111)
        dataTime = self.get_data(cycleNum, 'Time')
        for dataName in dataNameList:
            data = self.get_data(cycleNum,dataName)
            plt.plot(dataTime, data, label=dataName)    
        plt.xlabel('Time')
        plt.legend(loc='best')
    def compare_cycle(self, cycleList, dataName):
#        Visualization of difference of the 'dataName' for different cycles which represent different stage of battery lifetime
        fig1 = plt.figure()
        fig1.add_subplot(111)
        for cycle in cycleList:
            dataTime = self.get_data(cycle, 'Time')
            data = self.get_data(cycle, dataName)
            plt.plot(dataTime,data, label= 'cycle number: '+str(cycle))
        plt.xlabel('Time')
        plt.legend(loc='best')
        plt.title('Comparison of '+dataName)
    def get_data_names(self,cycleNum):
        return self.matData['cycle'][0,0][0,cycleNum]['data'][0,0].dtype.names
    
    def format_data_to_dic(self, cycleNum):
#        convert the multilevel data to a single level dictionary 
        dataNameList = self.get_data_names(cycleNum)
        
        dic = {'cycleIndex': cycleNum, 'type': self.get_type, 'ambient_temperature': self.get_ambient_temperature}
        for dataName in dataNameList:
            dic[dataName] = self.get_data(cycleNum, dataName)
        return dic