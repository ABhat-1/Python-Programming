class College(object):
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

class Student(College):
    def __init__(self,name,idnumber,course,subject):
        self.course=course
        self.subject=subject
        College.__init__(self,name,idnumber)
    def display(self):
        print(self.course)
        print(self.subject)
a=College('Shreya','ab001004')
b=Student('Shreya','ab001004','MS','Python')
a.display()
b.display()
