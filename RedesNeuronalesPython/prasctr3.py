# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 10:18:26 2022

@author: sala8
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def plano3d(intx,inty, intz):
    puntos= [  [ float(intx), 0 , 0 ],
               [ 0 ,  float(inty), 0], 
               [ 0 , 0 , float(intz)]    ]
    punto0, punto1, punto2= puntos 
    
    Ax,Ay,Az=punto0
    Bx,By,Bz=punto1
    Cx,Cy,Cz=punto2
    
    ABx,ABy,ABz= [Bx-Ax,By-Ay,Bz-Az]
    ACx,ACy,ACz= [Cx-Ax,Cy-Ay,Cz-Az]
    ABcruzAC= [ABy * ACz - ABz * ACy, ABz * ACx - ABx * ACz, ABx * ACy - ABy * ACx]
    
    punto= np.array(punto0)
    vectorNormal= np.array(ABcruzAC) 
    d= -punto.dot(vectorNormal)
    
    xx,yy=np.meshgrid(range(-5,5),range(-5,5))
    z= (-vectorNormal[0]*xx-vectorNormal[1]*yy-d)* 1. /vectorNormal[2]
    return xx,yy,z

p = np.array(([3,1,-1],[-2,-2,2],[-3,-1,1]))

t = np.array(([0],[1],[1]))

w = np.random.rand(3)
b = np.random.rand(1)

epoca = 5

for i in range(epoca):
    for j in range(len(p)):
        n = np.dot(np.transpose(w),p[j])+b
        if n<0:
            a=0
        else:
            a=1
        e = t[j] - a
        w = w + p[j]*e
        b = b + e
        
print(w)
print(b)

intx = (-b)/w[0]
inty = (-b)/w[1]
intz = (-b)/w[2]


xx,yy,z = plano3d(intx,inty,intz)

plt3d=plt.figure().gca(projection='3d')
plt3d.plot_surface(xx,yy,z, alpha = 0.8, color = 'yellow')
plt.show()


for i in range(len(p)):
    if i <1:
        plt3d.plot(np.int0(p[i][0]),np.int0(p[i][1]),np.int0(p[i][2]),marker="o",color="blue")
    else:
        plt3d.plot(np.int0(p[i][0]),np.int0(p[i][1]),np.int0(p[i][2]),marker="*",color="green")
    
