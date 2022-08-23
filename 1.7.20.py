num=int(input("Enter a number:"))
temp=num
count=0
while num>0:
    count=count+1
    num=num//10
print("The number of digits in",temp,"are", count)
    
