try:
    num=int(input("Enter a positive number:"))
    if num<0:
        raise ValueError("Not a positive number.Enter a positive number")
except ValueError as vee:
    print(vee)
