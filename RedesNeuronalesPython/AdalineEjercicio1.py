# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 08:46:16 2022

@author: Sala1
"""

import numpy as np
import matplotlib.pyplot as plt

p = np.array(([0,0], [0,1], [1,0], [1,1]))

t = np.array([-1,1,1,1])

w = np.zeros(2)
b = np.zeros(1)
epoc = 1000


R = 0
for i in range(len(p)):
    R=R+0.25*np.outer(p[i],np.transpose(p[i]))
    #print(R)

eigenvalor,vector=np.linalg.eig(R)
landamax=max(eigenvalor)
alpha=1/(4*landamax)*0.99



for i in range(epoc): 
    for j in range(len(p)):
        a = np.dot(w,p[j]) + b
        e = t[j]-a
        w=w+alpha*(np.outer(e,p[j]))
        b=b+alpha*e
        
print("Peso es: ", w[0])
print("Polarización es: ", b)

intx= (-b)/(w[0,0])
inty= (-b)/(w[0,1])

m = (inty-0)/(0-intx)
x=np.arange(-3,3,.1)
y=m*x+inty


#Graficas

plt.figure(1)
for i in range(len(p)):
    if i <1:
        plt.plot(np.int0(p[i][0]),np.int0(p[i][1]),marker="o",color="blue")
    else:
        plt.plot(np.int0(p[i][0]),np.int0(p[i][1]),marker="o",color="green")

plt.plot(x,y)
plt.xlim(-2,2)
plt.ylim(-2,2)
plt.plot(w[0,0],w[0,1])
plt.arrow(0,0,w[0,0],w[0,1],head_width=0.2,head_length=0.2)
plt.title('Entrenamiento Perceptron')
plt.legend(bbox_to_anchor=(0.9,1), loc='upper left',borderaxespad=0.1)
plt.grid(True)
