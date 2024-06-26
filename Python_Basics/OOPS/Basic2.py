
class SampleWord():
    pass

my_sample = SampleWord()
print(my_sample)


class Dog():

    #class object attribute
    species = 'mammal'

    # first method act as a constructor
    def __init__(self,mybreed,name):

        #user defined attributes
        self.breed = mybreed
        self.name = name

    # Operations/actions -- methods
    def bark(self,number):
        print('WOOF!')
        print("WOOF! My name is {} and the number is {}".format(self.name,number))



my_dog = Dog(mybreed='Lab',name='Sammy')

print(my_dog.breed)
print(my_dog.name)
print(my_dog.species)

print(my_dog.bark)
print(my_dog.bark(12))
