oddnumbers=set([x*2+1 for x in range(1,10)])
print(oddnumbers)
primenum=set()
flag=1
for n in range(2,30):
    m=2
    flag=0
    while m<=n/2:
        if n%m==0:
            flag=1
        m+=1
    if flag==0:
        primenum.add(n)   
    
print(primenum)
print("\n")
print("UNION")
print(oddnumbers.union(primenum))
print("\n")
print("INTERSECTION")
print(oddnumbers.intersection(primenum))
print("\n")
print("DIFFERENCE")
print(oddnumbers.difference(primenum))
print("\n")
print("SYMMETRIC DIFFERENCE")
print(oddnumbers.symmetric_difference(primenum))





