# -*- coding: utf-8 -*-
"""
Created on Thu May  3 11:08:23 2018

@author: zha200
"""

#import math as mth
#import sys
#import scipy.io as sio
import utility_battery as ub
import matplotlib.pyplot as plt
#import numpy as np
#import pandas as pd

numCycle = 0
B0005 = ub.MatFileLoader('B0005')
#dataTime = B0005.get_data(numCycle,'Time') 
#dataVoltage = B0005.get_data(numCycle,'Voltage_measured') 
#dataCurrent = B0005.get_data(numCycle,'Current_measured') 
#dataVoltageChar = B0005.get_data(numCycle,'Voltage_charge') 
#dataCurrentChar = B0005.get_data(numCycle,'Current_charge') 
#cycleTime = B0005.get_time(numCycle) 
#cycleType = B0005.get_type(numCycle)

## illustration
#fig1 = plt.figure()
#ax1 = fig1.add_subplot(111)
#line1 = plt.plot(dataTime,dataVoltage, label='battery voltage', linestyle='--')
#line2 = plt.plot(dataTime,dataVoltageChar,label='charger voltage')
#plt.legend(loc='best')
#plt.xlabel('Time')

#-----
#B0005.plot_data(numCycle,['Voltage_measured','Voltage_charge'])
#B0005.plot_data(numCycle,['Current_measured','Current_charge'])

print(B0005.format_data_to_dic(numCycle))
  
