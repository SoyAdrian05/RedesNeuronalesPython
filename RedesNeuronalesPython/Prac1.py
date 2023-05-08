# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

p = np.array(([0,0], [0,1], [1,0], [1,1]))

t = [0,1,1,1]

w = np.random.rand(2)
b = np.random.rand(1)
epoc = 100

for i in range(epoc): 
    for j in range(len(p)):
        n = np.dot(np.transpose(w),p[j]) + b
        if n<0:
            a=0
        else: 
            a=1
        e = t[j] - a
        w = w + p[j]*e 
        b = b + e

print(w)
print(b)
            
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