class Age(Exception):
    def display(self):
        print("Not eligbible for voting")
try:
    age=int(input("Enter age:"))
    if age<18:
        raise Age
except Age as a:
    a.display()
else:
    print("Eligible for voting")
