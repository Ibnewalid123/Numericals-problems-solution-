'''this is a simulation of the dillema happened in that video. https://youtu.be/iSNsgj1OCLA?feature=shared  kinda blowing my mind '''



import numpy as np

result=[]
for k in range(10):

    success=0
    N=1000

    for _ in range(N):

        count=[]
        matrix=np.arange(0,100)
        matrix_=matrix
        np.random.shuffle(matrix_)

        for i in matrix:
            attempt=0
            j=i

            while attempt<=50:

                if j== matrix_[i]:
                    count.append(i)
                    break
                else:
                    i=matrix_[i]

                attempt=attempt+1

        if len(count)==100:
            success=success+1
    result.append(success/N)
    

np.mean(result)
