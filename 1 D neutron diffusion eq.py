import numpy as np 
import math
import matplotlib.pyplot as plt 

#mesh size and other data 
sigma_a=0.2
Q=10
D=1

h=0.01
a=5
n=int(1/h)
x=np.linspace(-a,a,int(n))

'''creating nxn zero matrix '''

A=np.zeros((n,n))

for i in range (int(n)):
    for j in range (int(n)):
        if i==j:
            A[i][j]=-1
        if j-1<n and j==i and j>0:
            A[i][j-1]=sigma_a*h**2+2
            
        if j-2<n and i==j and j>0:
            A[i][j-2]=-1

print(A)
constant=np.zeros(n)
for i in range(n):
    constant[i]=Q*h**2/D

"""print(constant)""" 
from scipy.linalg import solve
s=solve(A,constant)

plt.figure(figsize=(10,6))
plt.plot(x,s,marker='*',color='red')
