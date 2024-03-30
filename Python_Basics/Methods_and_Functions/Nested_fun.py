x = 25

def printer():
    x = 50
    return x

print(x)
print(printer())

#local var - num
result1 = lambda num:num**2
print(result1(4))

#------

#GLOBAL
name = 'THIS IS A GLOBAL STRING'

def greet():

    #ENCLOSING
    name = 'Sammy'

    def hello():
        #LOCAL
        name = 'IM A LOCAL'
        print('Hello '+name)

    hello()

greet()


#---  scope

x = 50

def funcX(x):
    print(f'X is {x}')

    x = 'NEW VALUE'
    print(f'I JUST LOCALLY CHANGED GLOBAL X TO {x}')
    print(x)
    return x

result = funcX(100)
print(result)

#------ with global keyword

y = 50

def funcY():
    global y
    print(f'Y is {y}')

    #local reassignment on a global variable!
    y = 'NEW VALUE'
    print(f'I JUST LOCALLY CHANGED GLOBAL Y TO {y}')
    print(y)

funcY()

print("x = ",x)
print("y = ",y)

