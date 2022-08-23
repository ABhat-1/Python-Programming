import math
a= int(input("Enter the value of a:"))
b= int(input("Enter the value of b:"))
c= int(input("Enter the value of c:"))
d = b**2 - 4*a*c

if d<0:
    print("No solution")
    
if d==0:
    root1=(-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    print("One solution",root1)
    
else:
     root1=(-b + math.sqrt(b**2 - 4*a*c))/(2*a)
     root2=(-b - math.sqrt(b**2 - 4*a*c))/(2*a)
     print("The two solutions are {} and {}".format(root1, root2))
     
    
