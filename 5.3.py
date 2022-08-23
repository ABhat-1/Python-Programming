ul=int(input("Enter the maximum number for which you want prime numbers:"))
for x in range(2,ul+1):
    p=0
    for i in range(2,x//2+1):
        if(x%i==0):
            p=p+1
    if(p<=0):
        print(x)
        
