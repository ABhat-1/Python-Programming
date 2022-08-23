def swap(a,b):
    temp=a
    a=b
    b=temp
    print("The values of a and b after swapping are",a,b)
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print("The values of a and b before swapping are",a,b)
swap(a,b)
