num=int(input("Enter the numerator:"))
den=int(input("Enter the denominator:"))
try:
    quo=num/den
    print("The quotient is:",quo)
except ZeroDivisionError as ZDE:
    print(ZDE)
