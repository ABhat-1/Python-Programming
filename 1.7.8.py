import math
a=float(input("Enter the value of the first side of the triangle:"))
b=float(input("Enter the value of the second side of the triangle:"))
c=float(input("Enter the value of the third side of the triangle:"))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of the triangle is",round(area,2))
