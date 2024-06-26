
#3
def myfunc(boolval):
    if boolval == True:
        print("Hello")
    if boolval == False:
        print("Goodbye")
    else:
        pass

myfunc(False)

#4
def myfunc(x,y,z):
    if(z == True):
        return x
    if(z == False):
        return y
    
result = myfunc(123,10,True)
print(result)

#5
def myfunc(no1,no2):
    return no1+no2

result = myfunc(10,20)
print(result)

#6
def is_greater(a,b):
    return a>b

result = is_greater(7,6)
print(result)

#7
def Print_Name(name):
    print("Your name is : {}".format(name))
    print(f"Your name is : {name}")

Print_Name('aniket')




# args assignment
#pick evens

even_list = []
def check_even(*args):
    for number in args:
        if number % 2 == 0:
            even_list.append(number)
        else:
            pass
    return even_list

check_even(1,2,3,4,5,6,7,8,9)
print(even_list)

def check_even2(*args):
    even_list2 = [num for num in args if num%2==0]
    return even_list2

result = check_even2(1,2,3,4,5,6,7,8,9)
print(result)


#10 skyline :

def myfunc(string1):
    index = 0
    string2 =''
    while(index<len(string1)):
        if(index %2 == 0):
            string2 = string2+string1[index].upper()
        else:
            string2 = string2+string1[index].lower()
        
        index = index +1
    return string2

result = myfunc('aniket')
print(result)
