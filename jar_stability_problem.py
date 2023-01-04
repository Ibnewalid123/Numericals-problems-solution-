import numpy as np

r_b=[]
b_b=[]

for i in range (100):
    current_balls=1300
    lal_ball=0
    nil_ball=0
    r=300
    b=1000
    for j in range(300):
        
        ball=np.random.choice(["red","blue"],p=[r/current_balls,b/current_balls])
        if ball=="red":
            lal_ball=lal_ball+1
            r=r-1
        else:
            nil_ball=nil_ball+1
            b=b-1
        current_balls=current_balls-1
            
    r_b.append((700+lal_ball)/1000)
    b_b.append((1000-nil_ball)/1000)
    
print(np.mean(r_b),"     ",np.mean(b_b))
