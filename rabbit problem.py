#our second representation will be rate vs equilibrium position 

import numpy as np 
import matplotlib.pyplot as plt 

def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num


growth_factor=np.linspace(1,8,10)

equilibrium_population=[]
#new project 
#logistic map and the birth problem of rabbits 
#first let us make a graph 
#the main equation is Xn+1=meu*X(1-X)
#where meu is the growth factor
#1000 times iteration then taking eqilibrium_population.append(y[999])
y0=0.6
n=0
while n<10:
    y=[]
    for i in range(100):
        y.append(growth_factor[n]*y0*(1-y0))
        y0=y[i]
        
    a=most_frequent(y)    
    equilibrium_population.append(a)
    n=n+1    
    
plt.figure(figsize=(16,10))
plt.plot(growth_factor,equilibrium_population,color='red',linewidth=0.9)
plt.xlabel("Meu")
plt.ylabel("Equilibrium Populations")
