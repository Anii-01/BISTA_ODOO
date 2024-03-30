class Animal():
    def __init__(self,name):
        self.name = name

    # Abstraction - abstract method
    def speak(self):
        raise NotImplementedError("Subclas must implemented this abstract method")
    
class Dog(Animal):
    def speak(self):
        return self.name+ " says woof!"
    
class Cat(Animal):
    def speak(self):
        return self.name+ " says meow!"

fido = Dog('Fido')
isis = Cat("Isis")

print(fido.speak())
print(isis.speak())