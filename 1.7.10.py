string=input("Enter the string:")
string=string.casefold()
reverse_string=reversed(string)
if list(string)==list(reverse_string):
    print(string,"is a palindrome")
else:
    print(string, "is not a palindrome")
