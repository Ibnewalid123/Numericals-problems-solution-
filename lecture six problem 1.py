#problem no lecture six (1)

import numpy as np 
import matplotlib.pyplot as plt 

x=[]
y=[]

theta=np.linspace(-math.pi*10,math.pi*10,num=2000)
#theta=theta.tolist()
k=0.05
i=0
while i<2000:
    x.append(math.cos(theta[i])*math.e**(k*theta[i]))
    y.append(math.sin(theta[i])*math.e**(k*theta[i]))
    i=i+1
plt.figure(figsize=(8,6))
plt.plot(x[:1000],y[:1000],color='red',marker='.')
plt.plot(x[1000:],y[1000:],linewidth=0.8,color='green')