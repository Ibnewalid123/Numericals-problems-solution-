#this is jacobi iteration 
"""i will be accepting a matrix and solving it """

"""importing necessary libaries """
import numpy as np



def jacobi_solver (matrix,constant_vector,epsilon,initial_guess=None):

    """checking if the linear system has any solutions """

    if np.linalg.det(matrix)!=0:

        matrix=matrix
        b=constant_vector
        epsilon=epsilon
        if initial_guess==None:

            x1=np.zeros(len(b))

        else:
            x1=initial_guess
            print(x1)

        x2=np.zeros(len(b))

        m,n=np.shape(matrix)
        
        iteration=0
        logic=False

        """convergece = abs (x(k+1)-x(k))/x(k+1)"""

        while logic==False :
            iteration=iteration+1

            """             first we need to check the algorithm again 

            Xi(k+1)=(b[i]-sum(a[i][j]*X[j](k)) and here i can't be equal to j )/a[i][i]
            
        """
            for i in range(m):
                sum=0

                for j in range(n):
                    """there should be an if statement which will ensure that i is not = j """
                    if i!=j:
                        sum=sum+matrix[i][j]*x1[j]
                
                x2[i]=(b[i]-sum)/matrix[i][i]

            
            convergence=abs (x2[i]-x1[i])/x2[i]
            if convergence < epsilon:
                logic=True
            
            x1= x2.copy()
            
        print(iteration)
        return x1
    else:
        print("solution of this matrix is not available ")

matrix=[[4, -1., 0., 0., 0.],
       [-1, 4, -1, 0., 0.],
       [0., -1, 4, -1, 0.],
       [0., 0., -1, 4, -1.],
       [0., 0., 0., -1, 4]]
b=[100,100,100,100,100]
jacobi_solver(matrix,b,10**-10)
