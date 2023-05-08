# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 21:15:58 2022

@author: Adrian
"""

# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt 
import numpy as np
import matplotlib.pyplot as plt

p = np.array(([0,0], [0,1], [1,0], [1,1]))

t = [0,1,1,1]

wt = np.zeros(2)
w = np.transpose(wt)
b = np.random.rand(1)
epoc = 5
#epoc = int(input("Inserte el número de epocas: "))
R=0

def corr(r):
    eigenvalor,vector=np.linalg.eig(r)      
    landamax=max(eigenvalor)
    return 1/(4*landamax)*0.99

for j in range(len(p)):
    R = R + 0.25*np.outer(p[j],np.transpose(p[j]))
    alpha=corr(R)
    print(alpha)
        

for i in range (epoc):
    for j in range(len(p)):
        a = np.dot(w,p[j])+b
        print(b)
        error= np.float64(t[j]-a)
        w=w+ alpha*(np.dot(error,p[j]))
        b=b+alpha*error

print("w es: ",w)
print("B es: ", b)       


intx= (-b)/(w[0])
inty= (-b)/(w[1])

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
plt.plot(w[0],w[1])
plt.arrow(0,0,w[0],w[1],head_width=0.2,head_length=0.2)
plt.title('Entrenamiento Perceptron')
plt.legend(bbox_to_anchor=(0.9,1), loc='upper left',borderaxespad=0.1)
plt.grid(True)
