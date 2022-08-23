try:
    num=int(input("Enter a number:"))
    if(num>0):
        print(num)
    else:
        raise ValueError("Enter a positive integer")
except ValueError as e:
    print(e)
