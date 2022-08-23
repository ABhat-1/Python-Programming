P1=int(input("Enter first number:"))
P2=int(input("Enter second number:"))
P3=int(input("Enter third number:"))
if P1 > P2:
    if P1 > P3:
        maxNum = P1
    else:
        maxNum = P3
elif P2 > P3:
        maxNum = P2
else:
    maxNum = P3
print("The maximum number among the three is", maxNum)
