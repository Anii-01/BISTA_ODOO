
class SampleWord():
    pass

my_sample = SampleWord()
print(my_sample)


class Dog():

    #class object attribute
    species = 'mammal'

    # first method act as a constructor
    def __init__(self,mybreed,name,spots):

        #user defined attributes
        self.breed = mybreed
        self.name = name
        self.spots = spots


my_dog = Dog(mybreed='Lab',name='Sammy',spots='No Spots')
#type(my_dog)

print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
