# -*- coding: utf-8 -*-
"""
Created on Sat Mar 05 17:29:54 2016

@author: kamal
"""

import numpy as np
import matplotlib.pyplot as plt

N=2
M=9
np.random.seed(0)
xdata=np.random.random_sample(N)
fun= lambda x: np.sin(2*np.pi*x)
std=0.1
mean=1
ydata=fun(xdata)*np.random.normal(mean,std,N)

plt.plot(xdata,ydata,'ro',label='actual data')
x=np.linspace(0,1,100)
y=fun(x)
plt.plot(x,y,label='best fit data')
alpha=5e-3
beta=11.1
newdata=zip(xdata,ydata)

phi=lambda x: np.matrix([ x**i for i in range (M+1)]).T
mu=[]
top=[]
bottom=[]
xs=np.linspace(0,1,100)
for num in xs:
    S=(alpha*np.eye(M+1)+beta*sum(phi(xdata)*phi(xdata).T for xdata,ydata in newdata)).I
    s=np.sqrt(1./beta+phi(num).T*S*phi(num)).item(0,0)
    m=(beta*phi(num).T*S*sum(phi(xdata)*ydata for xdata,ydata in newdata)).item(0,0)
    mu.append(m)
    top.append(m+s)
    bottom.append(m-s)
    
plt.plot(xs,mu,'k',label='mean value')
plt.ylim([-1.5,1.5])
plt.fill_between(xs,top,bottom,color='lightgray')
plt.legend()
    
    

