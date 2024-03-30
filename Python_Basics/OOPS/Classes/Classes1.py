
class Student:
    name = "defaul"
    department = "Computer"
    year = 2024

    def __init__(self,name,department,year):

        self.name = name
        self.department = department
        self.year = year
    
    def display_info(self):
        print("\n-----------Student Info-----------\n")
        print(" Name os student is : ",self.name ,"\n","Department is : ",self.department , "\n", "Year is : ",self.year)


std1 = Student("Aniket","Computer",2023)
print(std1)
print(std1.display_info)
print(std1.display_info())

print(std1.name)



