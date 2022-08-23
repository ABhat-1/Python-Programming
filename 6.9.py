def exp(a,b):
    if(b==0):
        return 1
    else:
        return(a*exp(a,b-1))
n=int(input("Enter the first number:"))
m=int(input("Enter the second number:"))
print("Result=",exp(n,m))
