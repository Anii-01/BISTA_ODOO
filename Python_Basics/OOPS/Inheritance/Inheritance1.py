class Animal():                               #Base class

    def __init__(self):
        print("ANIMAL CREATED!")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


class Dog(Animal):           #Dog inherit Animal     

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def who_am_i(self):           #method overriding
        print("I am a dog!")

    def eat(self):
        print("I am a dog eating")

    def bark(self):
        print("WOOF!")



   

mydog = Dog()
mydog.eat()
mydog.who_am_i()
mydog.bark()


