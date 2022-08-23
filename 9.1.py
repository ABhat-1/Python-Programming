class parent1(object):
    def __init__(self):
        self.str1="parent1"
        print("parent1")

class parent2(object):
    def __init__(self):
        self.str2="parent2"
        print("parent2")

class derived(parent1,parent2):
    def __init__(self):
        parent1.__init__(self)
        parent2.__init__(self)
        self.str3="derived"
        print("derived")

    def printStrs(self):
        print(self.str1,self.str2,self.str3)
ob=derived()
ob.printStrs()
        
