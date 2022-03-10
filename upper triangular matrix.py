#new assignmatrixment 
#lower matrix and upper matrix 

import numpy as np

matrix=[[1,2,3,4],
        [2,3,5,3],
        [5,6,3,5],
        [9,8,23,2]]
upper=matrix

#first upper matrix
row,col=np.shape(matrix)

#creating upper matrix 

for k in range(row-1):
    for i in range(k+1,row):
        if matrix[i][k] == 0:
            continue
        factor = matrix[k][k]/matrix[i][k]
        for j in range(k,col):
            matrix[i][j] = matrix[k][j] - matrix[i][j]*factor
        
matrix
