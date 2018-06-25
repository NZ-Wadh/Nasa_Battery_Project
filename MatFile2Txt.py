# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 14:57:18 2018

@author: zha200
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
import tensorflow as tf

def read_dataSet():
    #1. read segmented data stored in txt file 
    # for V columns, normalize w.r.t Vn = 3.2V
    # for Q columns, change sign and normalize w.r.t   6600 (determined using idxmax)
    fileName = 'B0005.txt'
    normVol = 3.4
    normQ = 6600
    data = pd.read_table(fileName, sep=',', comment='#')
    data.iloc[:,1:11] = data.iloc[:,1:11].apply(lambda x: x/normVol)
    data.iloc[:,11:21] = data.iloc[:,11:21].apply(lambda x: -x/normQ)
#    get the features and results to X and y, respectively
    X = np.float32(data[data.columns[1:21]].values)
    y = np.float32(data[data.columns[0]].values)
    print(X.shape)
    return(X,y)

    
    
# read data
X,Y = read_dataSet()
# shuffle data into random order
X,Y = shuffle(X, Y, random_state = 1)
# spllit the data into training and testing dataset
train_x, test_x, train_y, test_y = train_test_split(X,Y, test_size = 0.2, random_state=415)
print('Shape of training feature train_x is ', train_x.shape)
print('Shape of testing feature test_x is ', test_x.shape)

# definie linear regression model:


#linear_regression_model = tf.estimator.LinearRegressor(feature_columns=train_x)
#STEPS = 1000
#linear_regression_model.train()

# building the computational graph
n_sam = train_x.shape[0]
n_dim = train_x.shape[1]
learning_rate = 0.01
training_epochs = 1000
cost_history = np.empty(shape = [1], dtype=float)

# the linear regression model
tfX = tf.placeholder(tf.float32, [n_sam, n_dim])
tfY = tf.placeholder(tf.float32, [n_sam])
W = tf.Variable(tf.ones([n_dim,1], tf.float32),tf.float32)
b = tf.Variable([-0.3], tf.float32)
init = tf.global_variables_initializer()

pro = tf.matmul(tfX,W)
y_ = tf.add(pro, b)

# the cost function mse, and the optimization algorithm: gradient descent
cost = tf.reduce_mean(tf.square(y_-Y))
training_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# start the flow and train
sess = tf.Session()
sess.run(init)
training_epochs = 1000

for epoch in range(training_epochs):
    print('------process is ', epoch)
    sess.run(training_step, feed_dict = {tfX:train_x, tfY: train_y})
    cost_history = np.append(cost_history, sess.run(cost, feed_dict = {tfX:train_x, tfY:train_y}))


# illustration of result
plt.plot(range(len(cost_history)), cost_history)
plt.axis([0, training_epochs, 0, np.max(cost_history)])
plt.show()

