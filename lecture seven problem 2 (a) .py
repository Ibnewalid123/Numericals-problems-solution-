#problem from lecture 7 2(a)

import numpy as np 

n=10

matrix=np.zeros((n,n))

for i in range (n): 
    #first loop will be rows 
    #first 1st row then 2nd row and on on 
    for j in range (n): 
        #2nd loop will be colum 
        if (i==j):
            matrix[i][j]=i+1

print(matrix)