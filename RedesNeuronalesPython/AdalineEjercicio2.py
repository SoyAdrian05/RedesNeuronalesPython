# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 09:12:09 2022

@author: Sala1
"""

import numpy as np
import matplotlib.pyplot as plt


p = np.array(([-2,0],[0,1],[0,-1],[3,2],[4,1],[4,3],[4,-2],[3,-3]))

t = np.array(([1,1],[1,1],[1,1],[-1,1],[-1,1],[-1,1],[1,-1],[1,-1]))

w1 = np.zeros((2,1))
w2 = np.zeros((2,1))
b1 = np.zeros(1)
b2 = np.zeros(1)
b = np.zeros(2)
w = np.zeros((2,2))

a = np.zeros(2)

epocas = 50

R = 0
for i in range(len(p)):
    R=R+0.25*np.outer(p[i],np.transpose(p[i]))
    #print(R)

eigenvalor,vector=np.linalg.eig(R)
landamax=max(eigenvalor)
alpha=1/(4*landamax)*0.99
print(alpha)

#
for i in range(epocas): 
    for j in range(len(p)):
        a1 = np.dot(np.transpose(w1),p[j]) + b1
        e1 = t[j][0] - a1
        w1 = w1 + np.outer(p[j],e1)*alpha 
        b1 = b1 + e1

for i in range(epocas): 
    for j in range(len(p)):
        a2 = np.dot(np.transpose(w2),p[j]) + b2
        e2 = t[j][1] - a2
        w2 = w2 + np.outer(p[j],e2)*alpha
        b2 = b2 + e2

w = np.concatenate((w1,w2),axis=1)
b = np.concatenate((b1,b2))
print(w)

#for j in range(epocas):
#    for i in range(len(p)):
#        for k in range(len(a)):
#            a1 = np.dot(w1,np.transpose(p[i])) + b1
#            a2 = np.dot(w2,np.transpose(p[i])) + b2
#            e1 = t[i][k] - a1
#            w1 = w1 + np.outer(e1,p[i])*alpha#(e * p[i])*alpha
#            b1 = b1 + e1
#            e2 = t[i][k] - a2
#            w2 = w2 + np.outer(e2,p[i])*alpha#(e * p[i])*alpha
#            b2 = b2 + e2


print("Peso 1 es: ", w1)
print("Polarización es: ", b2)
        
print("Peso 2 es: ", w2)
print("Polarización es: ", b2)


print("Peso es: ", w)
print("Polarización es: ", b)

   
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
