# function for addition
def addition(a, b):
    return a + b
# function for subtraction
def subtract(a, b):
    return a - b
# function for multiplication
def multiply(a, b):
    return a * b
# function for division
def division(a, b):
    return a / b
print("Select the choice.")
print("1.Addition")
print("2.Subtractraction")
print("3.Multiplication")
print("4.Division")
# accept user input 
choice = input("Enter choice(1 or 2 or 3 or 4):")
num1 = int(input("Type first number: "))
num2 = int(input("Type second number: "))
if choice == '1':
    print(num1,"+",num2,"=", addition(num1,num2))
elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
    print(num1,"/",num2,"=", division(num1,num2))
else:
    print("enter choice 1 to 4")
