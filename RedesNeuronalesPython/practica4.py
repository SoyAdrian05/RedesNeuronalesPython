# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 21:46:38 2022

@author: Adrian
"""


import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d
p=np.loadtxt('IrisDataBase.txt',usecols=(0,1,2))

fil = 150
col = 2

def sigmoid(x):
        return 1/(1+np.exp(-x))

def hardlimit(n):
    if n[0]<0:
        a[0]=0
    else:
        a[0]=1
    
    if n[1]<0:
        a[1]=0
    else:
        a[1]=1
t=np.zeros([fil,col])
for i in range(fil):
    if i<51:
        t[i]=[0,0]
    elif i>50 and i<101:
        t[i]=[1,0]
    else:
        t[i]=[0,1]
                 
w1 = np.zeros(3)
w2 = np.zeros(3)
b = np.zeros(2)
a = np.zeros(2)

epocas = 150
# n = np.dot(w,p[0])+b
# print(sigmoid(n))

for i in range(epocas):
    for j in range(len(p)):
        af=hardlimit(np.dot(w1,p[j])+b)
        e1 = t[j,k] - a[0]
        w1 = w1 + e1*np.transpose(p[j])#np.dot(p[j],e1)
            
            # print(w)
            #w = w + e*p[j]
        b[0] = b[0] + e1
            # print("\n",b)
            #print("\n",b)
        e2 = t[j,k] - a[1]
        w2 = w2 + e2*np.transpose(p[j])
        b[1] = b[1] + e2
            # print("\n",w1)
            # print("\n",e1)
            # print("\n",w2)
            # print("\n",e2)
               

print("W1: ", w1, "\n","W2: ",w2)
print("b1: ", w1, "\n","b2: ",w2)


# def comprobacion(peso):
#     for i in range(len(p)):
#         n1=np.dot((peso),p[i])+b
#         for k in range(len(a)):
#             if n1[k]<0:
#                 a[k]=0
#             else:
#                 a[k]=1
#         # print(a)
#         # print("\n",a==t[i])
        
# comprobacion(w)
            

intx1 = (-b[0])/w1[0]
inty1 = (-b[0])/w1[1]
intz1 = (-b[0])/w1[2]

x = np.linspace(-50,50,1)
y = np.linspace(-50,50,1)
z = np.linspace(-50,50,1)

u = x*intx1+y*inty1+z*intz1-b[0]
   

intx2 = (-b[1])/w2[0]
inty2 = (-b[1])/w2[1]
intz2 = (-b[1])/w2[2]

x1 = np.linspace(-3,3,1)
y1 = np.linspace(-3,3,1)
z1 = np.linspace(0,6,1)

u1 = x1*intx2+y1*inty2+z1*intz2-b[1]


fig = plt.figure()
# Creamos el plano 3D
ax1 = fig.add_subplot(111, projection='3d')
ax1.scatter(p[0:49,0], p[0:49,1],p[0:49,2], c='b', marker='o')
ax1.scatter(p[50:99,0], p[50:99,1],p[50:99,2], c='g', marker='o')
ax1.scatter(p[100:149,0], p[100:149,1],p[100:149,2], c='k', marker='o')


xx,yy=np.meshgrid(range(4, 10),range(2, 5))
z1=(b[0]-xx*intx1-yy*inty1)/intz1
ax1.plot_surface(xx,yy,z1, alpha=0.5)

xx1,yy1=np.meshgrid(range(5, 10),range(2, 5))
z2=(b[1]-xx1*intx2-yy1*inty2)/intz2
ax1.plot_surface(xx1,yy1,z2, alpha=0.5)

plt.show()