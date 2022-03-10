#gauss seidal method 
import numpy as np 

a=np.array([[20,1,-2],[3,20,-1],[2,-3,20]])
b=np.array([17,-18,25])

logic=False
x0,y0,z0=0,0,0

while logic==False:
    x=(1/a[0][0])*(b[0]-a[0][1]*y0-a[0][2]*z0)
    y=(1/a[1][1])*(b[1]-a[1][0]*x-a[1][2]*z0)
    z=(1/a[2][2])*(b[2]-a[2][0]*x-a[2][1]*y)
    y0=y
    z0=z
    if (x*a[0][0]+y*a[0][1]+z*a[0][2])==b[0]:
        logic=True
print(x,y,z)
