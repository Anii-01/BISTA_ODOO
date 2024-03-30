#__init__  method

'''
class Car:

    color = 'Blue'
    brand = 'Oddi'

car1 = Car()
print(car1.color)
print(car1.brand)

'''

#constructor

class Student:
    #name = "Karan"
    def __init__(self,name):               # if we not create this , python will automtically create this .. and it must have 1 self argument

        print(self)
        print("adding new student in database..")
        self.name = name

s1 = Student("Ram")
print(s1)
print(s1.name)

s2 = Student('karan')
print(s2.name)

