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

    
B0005 = ub.MatFileLoader('B0005')

#1. looking for the discharging cycles, index from 0
dischargeCycle = list()
for cycleNum in range(0,B0005.get_totalCycle()):
    if B0005.get_type(cycleNum) == 'discharge':
        dischargeCycle.append(cycleNum)
print('Total number of discharge cycle is ', len(dischargeCycle))


#2. define parameters to split the discharging curve into segments*
timeWindow = 100 # time window duration 100 s
timeStep = 20 # time slide step size 5 s
dataTimeDicList = list()
cycleNumIndex = 1
numPoints = 10  # number of points per piece of data

#3.prepare to write to txt file 
fileName = 'B0005.txt'
f = open(fileName,'w')
f.write('# data settings: timeWindow = ' + str( timeWindow)+ '# \n')
f.write('# data settings: timeStep = ' + str( timeStep)+ '# \n')
f.write('# data settings: numPoints = ' + str( numPoints)+ '# \n')
f.write('# data settings: \n')
f.write('# data 0: cycleNumber; data1-'+str(int(numPoints))+': voltage' + ' data'+ str(int(numPoints+1))
        +'-' + str(int(numPoints+numPoints))+ ': Q discharged \n')      
f.close()
fig1 = plt.figure()
fig1.add_subplot(111)

#4. split the discharge curve
for cycleNum in dischargeCycle:
#    print('------------cycle number is', cycleNum)
    print('------------Data Segmentation Progress is: %.0f' %float(cycleNumIndex/len(dischargeCycle)*100), '%-------------')
    voltageSeries = B0005.get_data(cycleNum, 'Voltage_measured')
    currentSeries = B0005.get_data(cycleNum, 'Current_measured')
    timeSeries = B0005.get_data(cycleNum, 'Time')
    QSeries = ub.DataPreparationTool().dischargeQ(currentSeries,timeSeries)['Q'] # calcualte discharge curve
    dataTimeDic = ub.DataPreparationTool().truncate(voltageSeries,currentSeries, QSeries, timeSeries) # remove curve when discharge current is 0 and voltage rise agian
    plt.plot(dataTimeDic['time'],dataTimeDic['voltage'])
#s segment discharge curve into segments and write to txt
    cycleNumIndex=cycleNumIndex+1 
    voltageDicList = ub.DataPreparationTool().segmentation(dataTimeDic['voltage'], dataTimeDic['time'], timeWindow, timeStep, numPoints)
    QDicList = ub.DataPreparationTool().segmentation(dataTimeDic['Q'],dataTimeDic['time'], timeWindow, timeStep, numPoints)
    ub.DataPreparationTool().WriteListOfDic2Txt(fileName,cycleNum,voltageDicList,QDicList)

plt.xlabel('Time')
#plt.legend(loc='best')
plt.grid()


# normalization 
# voltage: use 4.2: nominal cell voltage when fully charged.
# Q(SoC*): use the maximum Q of the first dicharging cylce(healthy state).
    
    
