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

# discharging cycles
numCycles2 = [2,98,182, 352,473, 614]
numCycles2 = [num-1 for num in numCycles2]

B0005.compare_cycle(numCycles2, 'Voltage_measured')
B0005.compare_cycle(numCycles2, 'Current_measured')