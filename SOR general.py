#this sor iteration 
"""i will be accepting a matrix and solving it """

"""importing necessary libaries """
import numpy as np


def succesive_over_relaxation (matrix,constant_vector,epsilon,initial_guess=None,over_relaxation_factor=1.1):

    """checking if the linear system has any solutions """

    if np.linalg.det(matrix)!=0:

        matrix=matrix
        b=constant_vector
        epsilon=epsilon
        omega=over_relaxation_factor

        if initial_guess==None:

            x1=np.zeros(len(b))

        else:
            x1=initial_guess
            print(x1)

        x2=np.zeros(len(b))

        m,n=np.shape(matrix)
        
        iteration=0
        c=0
        logic=False

        while logic==False:
            iteration=iteration+1

            """                  first we need to check the algorithm again 

            Xi(k+1)=(b-sum(a[i][j]*X(k)) and here i can't be equal to j )* omega /a[i][i] +(1-omega)*x(k)
            
        """
            for i in range(m):
                
                sum=0

                for j in range(n):

                    """there should be an if statement which will ensure that i is not = j """
                    if i!=j:
                        sum=sum+matrix[i][j]*x1[j]
            
                x2[i]=((b[i]-sum)*omega/matrix[i][i])+(1-omega)*x1[i]
                
                x1[i]=x2[i]
            

            convergence=abs (x2[i]-c)/x2[i]
            c=x2[i]
            if convergence<epsilon:
                logic=True
            
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
succesive_over_relaxation(matrix,b,10**-10,over_relaxation_factor=1.1)
