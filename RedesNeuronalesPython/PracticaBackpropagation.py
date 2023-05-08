#, -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 10:22:10 2022

@author: sala8
"""

import numpy as np
import matplotlib.pyplot as plt

plt.close("all")

def sigmoid(n):
    return 1/(1+np.exp(-n))

def pureline(n):
    return n*1

w1 = np.random.rand(2,1)
b1 = np.random.rand(2,1)
w2 = np.random.rand(1,2)
b2 = np.random.rand(1)

alpha = 0.01
patern = np.linspace(-2,2,9)
target=1+np.sin((np.pi/4)*patern)

epocas = 1500
ERROR = np.zeros(epocas*len(patern))
k = 0

for j in range(epocas):
    for i in range(len(patern)):
        a0 = patern[i]
        a1 = sigmoid(np.dot(w1,a0) + b1)
        a2 = pureline(np.dot(w2,a1) + b2) 
        error = target[i] - a2
        ERROR[k] = error**2
        
        #backpropagation
        df = 1
        s2 = -2*df*error
        df1 = np.diagflat(np.multiply((1-a1),(a1)))
        s1 = np.dot(df1,w1).dot(s2)
        #actualizacion
        w1 = w1 - alpha*s1*a0
        b1 = b1 - alpha*s1
        w2 = w2 - alpha*s2*a1.T
        b2 = b2 - alpha*s2
        
        k += 1
        
sal = np.zeros(len(patern))
# print(w1)
       
for i in range(len(patern)):
    a0 = patern[i]
    n1 = np.dot(w1,a0) + b1
    a1 = sigmoid(n1)
    n2 = np.dot(w2,a1) + b2
    sal[i] = pureline(n2)
    
    
y = target
plt.figure(1)
plt.plot(patern,target,"-o")
plt.plot(patern,sal)
plt.figure(2)
plt.plot(ERROR)
