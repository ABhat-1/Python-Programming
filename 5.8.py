def grcodi(a,b):
    while(b):
        a,b=b,a%b
    return a
a=int(input()) #get input from the user
b=int(input())
if(grcodi(a,b)==1):
    print("Co-prime")
else:
    print("Not prime") 
