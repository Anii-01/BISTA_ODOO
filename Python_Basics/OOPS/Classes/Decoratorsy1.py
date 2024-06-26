
def greet(fx):
    def mfx (*args,**kwargs):
        print("Good Morining")
        fx(*args,**kwargs)
        print("Thanks for using function")
    return mfx


@greet
def hello():
    print("Hello world")

@greet
def add(a,b):
    print(a+b)


#greet(hello())
hello()

greet(add(2,3))
add(2,5)