# -*- coding: utf-8 -*-
"""
Created on Thu May  3 11:08:23 2018

@author: zha200
"""

#import math as mth
#import sys
#import scipy.io as sio
import utility_battery as ub
import time
#import pandas as pd

#numCycle = 613
B0005 = ub.MatFileLoader('B0005')


# discharging cycles
numCycles2 = [2,98,182, 352,473, 614]
numCycles2 = [num-1 for num in numCycles2]

#B0005.compare_cycle(numCycles2, 'Voltage_measured')
#B0005.compare_cycle(numCycles2, 'Current_measured')

# chapter 2: feature extraction
# 2.1 Segmentation of cycle voltage and current
# interplation
voltageSeries = B0005.get_data(1, 'Voltage_measured')
timeSeries = B0005.get_data(1, 'Time')

# divide data into segments of 10 s duration (over-lapping/non over-lapping controlled by shift)
timeWindow = 100
timeStep = 5
startTime = time.time()
dataTimeDic = ub.DataPreparationTool().segmentation(voltageSeries, timeSeries, timeWindow, timeStep, 10)
print('Used time is: ', time.time()-startTime)
ub.DataPreparationTool().illustration([dataTimeDic['data'][2]],[dataTimeDic['time'][2]])