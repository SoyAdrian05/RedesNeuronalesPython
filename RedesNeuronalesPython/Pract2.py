# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 12:10:22 2022

@author: Adrian
"""

import numpy as np
import matplotlib.pyplot as plt


p = np.array(([-2,0],[0,1],[0,-1],[3,2],[4,1],[4,3],[4,-2],[3,-3]))

t = np.array(([1,1],[1,1],[1,1],[0,1],[0,1],[0,1],[1,0],[1,0]))

w = np.random.rand(2,2)
b = np.random.rand(2)

a = np.zeros(2)

# print(np.transpose(p))
# print(p[0])
epocas = 10000


for i in range(epocas):
    for j in range(len(p)):
        n = np.dot(w,p[j])+b
        for l in range(2):
            for k in range(len(a)):
                if n[k]<0:
                    a[k]=0
                else:
                    a[k]=1  
                e = t[j][l] - a
                #print(np.dot(e,p[j]))
                w = w + np.outer(e,p[j])
                b = b + e

for i in range(len(p)):
    n = np.dot(w,p[j])+b
    for l in range(2):
        for k in range(len(a)):
            if n[k]<0:
                a[k]=0
            else:
                a[k]=1  
            e = t[j][l] - a

                   

            
        
print(w)
print(b)
#print(b[1])


   
intx1= (-b[0])/(w[0,0])
inty1= (-b[0])/(w[0,1])
#print("X = ", intx1)
#print("Y = ",inty1) 
intx2= (-b[1])/(w[1,0])
inty2= (-b[1])/(w[1,1])
#print("X = ",intx2)
#print("Y = ",inty2)


m1 = (inty1-0)/(0-intx1)
x1=np.arange(-5,5,.1)
y1=m1*x1+inty1

m2 = (inty2-0)/(0-intx2)
x2=np.arange(-5,5,.1)
y2=m2*x2+inty2
#print(m1," ",m2)
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


plt.title('Entrenamiento Perceptron2')
plt.legend(bbox_to_anchor=(0.9,1), loc='upper left',borderaxespad=0.1)
plt.grid(True)
plt.show()