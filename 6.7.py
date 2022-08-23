def GCD(a,b):
    rem=a%b
    if rem==0:
        return b
    else:
        return GCD(b,rem)
n=int(input("Enter the first number:"))
m=int(input("Enter the second number:"))
print("The greatest common divisor of",n,"and",m,"is",GCD(n,m))

    
