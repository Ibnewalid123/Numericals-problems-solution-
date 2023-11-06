import numpy as np

def sort_matrix_by_column(matrix, column_to_sort=0):
    sorted_indices = np.argsort(matrix[:, column_to_sort])
    sorted_matrix=np.zeros_like(matrix)

    for i,index in enumerate(sorted_indices):
        sorted_matrix[i,:] = matrix[index,:]

    return sorted_matrix
