import numpy as np

matrix=np.array(
        [[10,-1,-2,0],
        [-1,11,-1,3],
        [2,-1,10,-1],
        [3,0,-2,8]])

#diagonal_matrix
def diagonal_matrix(matrix):
    m,n=np.shape(matrix)
    diagonal_matrix=np.zeros(np.shape(matrix))
    for i in range(m):
        for j in range(n):
            if j==i:
                diagonal_matrix[i][j]=matrix[i][j]
    return diagonal_matrix

#lower triangular matrix 
def lower_triangular_matrix(matrix):
    m,n=np.shape(matrix)
    lower_triangular_matrix=np.zeros(np.shape(matrix))
    for i in range(m):
        for j in range(n):
            if j<i:
                lower_triangular_matrix[i][j]=matrix[i][j]
    return lower_triangular_matrix

def Upper_triangular_matrix(matrix):
    m,n=np.shape(matrix)
    upper_triangular_matrix=np.zeros(np.shape(matrix))
    for i in range(m):
        for j in range(n):
            if j>i:
                upper_triangular_matrix[i][j]=matrix[i][j]
    return upper_triangular_matrix

def max_finder(matrix):
    m,n=np.shape(matrix)
    max=matrix[0][0]
    for i in range (m):
        for j in range (n): 
            if max< matrix[i][j]:
                max=matrix[i][j]   
            else:
                continue   

    return max   


T=np.matmul(np.linalg.inv(diagonal_matrix(matrix)-lower_triangular_matrix(matrix)),Upper_triangular_matrix(matrix))
#have to work on this line as i am not quite sure how many eigen array a linear system it can retrun 
eigen1,eigen2=np.linalg.eig(T)
eigen2=np.abs(eigen2)

max_finder(eigen2)
