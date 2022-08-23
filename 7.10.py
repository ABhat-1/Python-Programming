try:
    num=int(input("Enter an integer:"))
    raise ValueError
except ValueError as ve:
    print("Enter a valid integer")
    
