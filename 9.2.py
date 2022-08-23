class HOD(object):
    def __init__(self):
        print("HOD class")
        super(HOD,self).__init__()

class Teacher(object):
    def __init__(self):
        print("Teacher class")
        
class Student(HOD,Teacher):
    def __init__(self):
        super(Student,self).__init__()
        print('Student class')
S=Student()
        
