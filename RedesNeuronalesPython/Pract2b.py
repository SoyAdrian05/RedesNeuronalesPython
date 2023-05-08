# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 16:06:19 2022

@author: Adrian
"""

import numpy as np
import matplotlib.pyplot as plt


p = np.array(([-2,0],[0,1],[0,-1],[3,2],[4,1],[4,3],[4,-2],[3,-3]))

t = np.array(([1,1],[1,1],[1,1],[0,1],[0,1],[0,1],[1,0],[1,0]))

w1 = np.zeros(2)
w2 = np.zeros(2)

b1 = np.random.rand(1)
b2 = np.random.rand(1)

epoc = 1000

for i in range(epoc): 
    for j in range(len(p)):
        n = np.dot(np.transpose(w1),p[j]) + b1
        if n<0:
            a=0
        else: 
            a=1
        e1 = t[j][0] - a
        w1 = w1 + np.dot(p[j],e1) 
        b1 = b1 + e1

for i in range(epoc): 
    for j in range(len(p)):
        n = np.dot(np.transpose(w2),p[j]) + b2
        if n<0:
            a=0
        else: 
            a=1
        e2 = t[j][1] - a
        w2 = w2 + np.dot(p[j],e2) 
        b2 = b2 + e2


         
print(w1," ",b1)
print(w2," ",b2)

 
intx1= (-b1)/(w1[0])
inty1= (-b1)/(w1[1])
print("X = ", intx1)
print("Y = ",inty1) 
intx2= (-b2)/(w2[0])
inty2= (-b2)/(w2[1])
print("X = ",intx2)
print("Y = ",inty2)


m1 = (inty1-0)/(0-intx1)
x1=np.arange(-5,5,.1)
y1=m1*x1+inty1

m2 = (inty2-0)/(0-intx2)
x2=np.arange(-5,5,.1)
y2=m2*x2+inty2
print(m1," ",m2)
# Graficas

plt.figure()
for i in range(len(p)):
    if i <3:
        plt.plot(np.int0(p[i][0]),np.int0(p[i][1]),marker="o",color="blue")
    elif i>=3 and i<=5:
        plt.plot(np.int0(p[i][0]),np.int0(p[i][1]),marker="o",color="green")
    else: 
        plt.plot(np.int0(p[i][0]),np.int0(p[i][1]),marker="o",color="red")
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.xlim(-10,10)
plt.ylim(-10,10)


plt.title('Entrenamiento')
plt.legend(bbox_to_anchor=(0.9,1), loc='upper left',borderaxespad=0.1)
plt.grid(True)
plt.show()