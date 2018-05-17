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
import numpy as np
#import pandas as pd

#numCycle = 613
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


#print(B0005.format_data_to_dic(numCycle))
#SC = 'Sense_current'
#BC = 'Battery_current'
#CR = 'Current_ratio'
#BI = 'Battery_impedance'
#RI = 'Rectified_Impedance'
#batteryImp = np.squeeze(B0005.get_data(40,RI))
#plt.plot(batteryImp)


# charging cycles 
#numCycles1 = [1,180, 350,471, 613]
#numCycles1 = [num-1 for num in numCycles1]
#
#
#B0005.compare_cycle(numCycles1, 'Voltage_measured')
#B0005.compare_cycle(numCycles1, 'Current_measured')

# discharging cycles
numCycles2 = [2,98,182, 352,473, 614]
numCycles2 = [num-1 for num in numCycles2]

B0005.compare_cycle(numCycles2, 'Voltage_measured')
B0005.compare_cycle(numCycles2, 'Current_measured')