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
#import pandas as pd
import itertools

#import time
def WriteListOfDic2Txt(cycleNum, volDicList,QDicList):
    f = open('B0005.txt', 'a+')
    for zippled in zip(volDicList, QDicList):
        f.write(str('%d'% cycleNum) + ',')
        v2print = zippled[0]['data']
        q2print = zippled[1]['data']
        for ele in itertools.chain(v2print, q2print[0:-1]):
            f.write(str(formatFloat(ele))+ ',')
        f.write(str(formatFloat(q2print[-1]))+'\n')
    f.close()
        

def formatFloat(inputNum):
    return '%.3f' % inputNum

#def Normalization(valueList, wrtToValue):
#    for iteree in itertools.chain(valueList):
#        float(iteree/wrtToValue)
    
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
timeStep = 20 # time slide step size 5 s
dataTimeDicList = list()
cycleNumIndex = 1
numPoints = 10 
# number of points per piece of data
f = open('B0005.txt','w')
f.write('# data settings: timeWindow = ' + str( timeWindow)+ '# \n')
f.write('# data settings: timeStep = ' + str( timeStep)+ '# \n')
f.write('# data settings: numPoints = ' + str( numPoints)+ '# \n')
f.write('# data settings: \n')
f.write('# data 0: cycleNumber; data1-'+str(int(numPoints))+': voltage' + ' data'+ str(int(numPoints+1))
        +'-' + str(int(numPoints+numPoints))+ ': Q discharged \n')      
f.close()
fig1 = plt.figure()
fig1.add_subplot(111)
for cycleNum in dischargeCycle:
    print('------------cycle number is', cycleNum)
    print('------------Data Segmentation Progress is: %.0f' %float(cycleNumIndex/len(dischargeCycle)*100), '%-------------')
    voltageSeries = B0005.get_data(cycleNum, 'Voltage_measured')
    currentSeries = B0005.get_data(cycleNum, 'Current_measured')
    timeSeries = B0005.get_data(cycleNum, 'Time')
    QSeries = ub.DataPreparationTool().dischargeQ(currentSeries,timeSeries)['Q']
#    plt.plot(timeSeries,voltageSeries)
    dataTimeDic = ub.DataPreparationTool().truncate(voltageSeries,currentSeries, QSeries, timeSeries)
    plt.plot(dataTimeDic['time'],dataTimeDic['voltage'])
    cycleNumIndex=cycleNumIndex+1 
    voltageDicList = ub.DataPreparationTool().segmentation(dataTimeDic['voltage'], dataTimeDic['time'], timeWindow, timeStep, numPoints)
    QDicList = ub.DataPreparationTool().segmentation(dataTimeDic['Q'],dataTimeDic['time'], timeWindow, timeStep, numPoints)
    WriteListOfDic2Txt(cycleNum,voltageDicList,QDicList)
#    dataTimeDicList.append(dicToAppend)

plt.xlabel('Time')
#plt.legend(loc='best')
plt.grid()


# normalization 
# voltage: use 4.2: nominal cell voltage when fully charged.
# Q(SoC*): use the maximum Q of the first dicharging cylce(healthy state).
    
    
