
def myfunc(no1,no2,no3,no4):
    return no1+no2+no3+no4

result = myfunc(10,20,30,40)
print("With normal args: ",result)



def myfunc(*args):
    print(args)
    return sum(args)

result = myfunc(40,60,100,200)
print("With *args : ",result)


def myfunc2(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print("fruit is present!")
    else:
        print('I didi not find any fruit here')


result2 = myfunc2(fruit='apple',vrggie='lettuce')
print("With **kwargs : ",result2)




def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0],kwargs['food']))

myfunc(10,20,30,fruit='orange',food='eggs',animal='dog')