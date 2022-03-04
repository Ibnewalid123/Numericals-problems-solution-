#our second representation will be rate vs equilibrium position 

import numpy as np 
import matplotlib.pyplot as plt 

growth_factor=np.linspace(0.1,5,10000)

equilibrium_population=[]

for i in growth_factor:
    m=np.random.ranf()
    
    for j in range (1000):
        m=i*m*(1-m)
        m=m
    equilibrium_population.append(m)
    
plt.figure(figsize=(10,6))
plt.scatter(growth_factor,equilibrium_population,color='red',marker='.')
plt.xlabel("Meu")
plt.ylabel("Equilibrium Populations")