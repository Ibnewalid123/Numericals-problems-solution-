#euler's method for solving differential equation 

#######################################################################################
#importing necessary libaries 
import math 
import numpy as np
import matplotlib.pyplot as plt 

######################################################################################
#this will be only applicable for 1st order differential equation 
#we will be solving the differential equation y'=x-y**2 with an initial condition y(0)=1
#so here f(x,y)=-y
#euler's method :

#y(k+1)=y(k)+f(x(k),y(k))*h
#y(k)=y(k+1)
#x(k)=x(k)+h 

##########################################################################################

#initial condition at x=0 y=1
x0=0
y0=1
h=0.01

#differential slope function 
def f(x,y):
    return x-y**2

#creating array for plotting graps 
x=([])
y=([])

for i in range(500):
    x.append(x0)
    y.append(y0)
    
    y_op=y0+f(x0,y0)*h
    y0=y_op
    x0=x0+h
print(x0,y0)
plt.figure(figsize=(10,6))
plt.plot(x,y)
