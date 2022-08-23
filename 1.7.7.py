import sys
max=int(input("Enter the maximum number for the series:"))
if max<0:
    print("Enter a valid number")
    sys.exit()

fib0=0
fib1=1
print("Fibonacci series upto",max,":")
print(fib0,end=" ")
print(fib1,end=" ")
i=2
while(i<max):
    fib=fib0+fib1
    print(fib,end=" ")
    fib0=fib1
    fib1=fib
    i=i+1
   
    
    






