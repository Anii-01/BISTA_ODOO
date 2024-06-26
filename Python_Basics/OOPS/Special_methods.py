mylist = [1,2,3]
print(len(mylist))

class Sample():
    pass

mysample = Sample()

print(mysample)
print(mylist)

class Book():

    def __init__(self,title,author,pages):

        self.title = title
        self.author = author
        self.pages = pages

    #Speical methods for string
    def __str__(self):                 #actual string representation
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return self.pages  #return length of the user defined obj
    
    def __del__(self):
        print("A book obj has been deleted")
        

b = Book('python rocks','Jose',200)
print(b)
#what is the string representation of b

print(str(b))

print(len(b))

del b

print(b)