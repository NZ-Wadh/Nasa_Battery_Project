# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 11:38:41 2018

@author: zha200
"""

# tensorflow training of neural network for predicting battery lifetime
# using discharging cycles

# data preparation
import utility_battery as ub
import matplotlib.pyplot as plt
#import time

B0005 = ub.MatFileLoader('B0005')

#1. looking for the discharging cycles, index from 0
dischargeCycle = list()
for cycleNum in range(0,B0005.get_totalCycle()):
    if B0005.get_type(cycleNum) == 'discharge':
        dischargeCycle.append(cycleNum)
print('Total number of discharge cycle is ', len(dischargeCycle))
#numCycles2 = [2,98,182, 352,473, 614]
#dischargeCycle = [num-1 for num in numCycles2]

#2. estimate the conjungate of the state of charge SoC*
timeWindow = 100 # time window duration 100 s
timeStep = 5 # time slide step size 5 s
dataTimeDicList = list()
cycleNumIndex = 1
numPoints = 10 
# number of points per piece of data
fig1 = plt.figure()
fig1.add_subplot(111)
for cycleNum in [480]:
    print('------------cycle number is', cycleNum)
    print('------------Data Segmentation Progress is: %.0f' %float(cycleNumIndex/len(dischargeCycle)*100), '%-------------')
    voltageSeries = B0005.get_data(cycleNum, 'Voltage_measured')
    currentSeries = B0005.get_data(cycleNum, 'Current_measured')
    timeSeries = B0005.get_data(cycleNum, 'Time')
    QSeries = ub.DataPreparationTool().dischargeQ(currentSeries,timeSeries)['Q']
    plt.plot(timeSeries,voltageSeries)
    dataTimeDic = ub.DataPreparationTool().truncate(voltageSeries,currentSeries, QSeries, timeSeries)
    plt.plot(dataTimeDic['time'],dataTimeDic['voltage'])
    cycleNumIndex=cycleNumIndex+1 
    dicToAppend = ub.DataPreparationTool().segmentation(dataTimeDic['voltage'], dataTimeDic['time'], timeWindow, timeStep, numPoints)
    dicToAppend['Q'] = ub.DataPreparationTool().segmentation(dataTimeDic['Q'],dataTimeDic['time'], timeWindow, timeStep, numPoints)['data']
    dataTimeDicList.append(dicToAppend)

plt.xlabel('Time')
plt.legend(loc='best')
plt.grid()
# normalization 
# voltage: use 4.2: nominal cell voltage when fully charged.
# Q(SoC*): use the maximum Q of the first dicharging cylce(healthy state).
    
    
