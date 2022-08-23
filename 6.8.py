def Fibonacci(k):
    if(k<2):
        return 1
    return Fibonacci(k-1)+Fibonacci(k-2)
k=int(input("Enter the number for which you want the Fibonacci series:"))
for i in range(k):
    print("Fibonacci(",i,")=",Fibonacci(i))
