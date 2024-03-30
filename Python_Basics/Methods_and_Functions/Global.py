x = 50
y = 100

def funcX():

    global x , y
    
    print(x)
    print(y)

    # LOCAL reassignment on a global var
    x = 111
    y = 222
    return x , y

result = funcX()
print(result)

print(x)
print(y)

def func2(a,b):
    return a+b

result = func2(x,y)
print(result)


