#Constructors

class Student:

    #default Constructors
    def __init__(self):
        pass
    #parameterized constructor
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("Adding new student in database..")

s1 = Student('Aniket',01)
print(s1.name)

s2 = Student('Nikhil',02)
print(s1.name)