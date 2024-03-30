class Dog():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says Woof!"

class Cat():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"

niko = Dog("niko")
felix = Cat("felix")

print(niko.speak())
print(felix.speak())

#how polymorphism-
def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)