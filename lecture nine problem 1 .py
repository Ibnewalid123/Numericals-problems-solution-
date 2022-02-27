#Problems for Lecture 9
#we have to find the roots of a qudratic equation given as ax^2+bx+c=0
#and use conditionls 

#first importing math 
import math

a=1
b=0
c=1

#here I can't take input because my stupid Jupyter Notebook doesn't work when i use the function input 
#that's why I am taking predefined values 

Determinat=b**2-4*a*c

if a==0:

    print("this is not a quadratic equation but solution is x= :",-c/b)

elif Determinat>=0:

    solution1=(-b+math.sqrt(Determinat))/2*a
    solution2=(-b-math.sqrt(Determinat))/2*a
    print(solution1,'    ',solution2)

else:
    
    print ("it has two imiginary roots: ")
    img_root1=''+str(-b)+' +'+str(math.sqrt(abs(Determinat))/2*a)+'i'
    img_root2=''+str(-b/2*a)+' -'+str(math.sqrt(abs(Determinat))/2*a)+'i'

    print(img_root1,'   ',img_root2)

