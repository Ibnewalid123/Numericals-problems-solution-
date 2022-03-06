#jacobi method 
a=[[20,1,-2],
   [3,20,-1],
   [2,-3,20]]
   
d=[17,-18,25]

#initial guess 
x0,y0,z0=0,0,0
#solution 
x,y,z=0,0,0

#iteration starts 
#x=(d[0]-y0*a[0][1]*z0*a[0][2])
logic=False

while logic==False: 
   #x.append(x0)
   #y.append(y0)
   #z.append(z0)
   x=x0
   y=y0
   z=z0
   x0=(d[0]-y0*a[0][1]-z0*a[0][2])/a[0][0]
   y0=(d[1]-x0*a[1][0]-z0*a[1][2])/a[1][1]
   z0=(d[2]-x0*a[2][0]-y0*a[2][1])/a[2][2]

   
   #if x[i]==x0 and y[i]==y0 and z[i]==z0:
   if x==x0 and y==y0 and z==z0:
      logic=True

print(x,y,z)
#print (x[i-1],y[i-1],z[i-1])















