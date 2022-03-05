#equation will be x**2-3=0
import math
import matplotlib.pyplot as plt 
a=-1
b=2
def f(x):
    return (x**2-2) 
for i in range (90):
    x=(a+b)/2
    if f(x)==0:
        break
    elif f(x)>0:
        b=x
    elif f(x)<0:
        a=x

print(x)
f(x),i+1
