#problem lecture six(2)

import numpy as np 
import matplotlib.pyplot as plt 

x1=[]
x2=[]
y=[]

theta=np.linspace(-math.pi/4,math.pi/4,num=1000)
i=0
while i<1000:
    x1.append(-1*math.cos(theta[i])*math.sqrt(2*math.cos(2*theta[i])))
    x2.append(math.cos(theta[i])*math.sqrt(2*math.cos(2*theta[i])))
    y.append(math.sin (theta[i])*math.sqrt(2*math.cos(2*theta[i])))
    i=i+1

plt.figure(figsize=(8,6))
plt.plot(x2,y,color='green',linewidth=0.9)
plt.plot(x1,y,linewidth=0.9,color='red')

plt.show()