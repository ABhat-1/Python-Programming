num=int(input("Enter a number\n"))
rev=0
temp=num
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
print("The reverse of",temp,"is",rev)
    
