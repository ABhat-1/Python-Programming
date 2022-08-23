class compare:
    def __init__(self,compare):
        self.compare=compare
    def __gt__(self,other):
        if(self.compare>other.compare):
               return True
        else:
            return False
obj1=compare(6)
obj2=compare(8)
if(obj1>obj2):
    print("obj1 is greater than obj2")
else:
    print("obj2 is greater than obj1")
    
            
