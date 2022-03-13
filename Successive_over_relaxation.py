#sor method 
#this is just a practice code trying to implement the algorithm 

import numpy as np

a=np.array([[20,1,-2],
   [3,20,-1],
   [2,-3,20]])
   
d=np.array([17,-18,25])

#initial guess 
x,y,z=0,0,0

#loop 
logic=False
weight_factor = 1.1

i=0
while logic==False:
    
    #calculation 
    x=weight_factor*(1/a[0][0])*(d[0]-a[0][1]*y-a[0][2]*z)+(1-weight_factor)*x
    y=weight_factor*(1/a[1][1])*(d[1]-a[1][0]*x-a[1][2]*z)+(1-weight_factor)*y
    z=weight_factor*(1/a[2][2])*(d[2]-a[2][0]*x-a[2][1]*y)+(1-weight_factor)*z

    if (x*a[0][0]+y*a[0][1]+z*a[0][2])==d[0]:
        logic=True
        
    #iteration count 
    i=i+1

print(x,y,z,i)
