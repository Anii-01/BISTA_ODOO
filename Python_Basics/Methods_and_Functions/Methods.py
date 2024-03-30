'''
class MyClass:

    def instance_method(self):
        print("This is an instance method")

obj = MyClass()
obj.instance_method() 


def Subtract (a, b):
	return (a-b)

print( Subtract(10, 12) ) 
print( Subtract(15, 6) ) 

mylist = [1,2,3]
#print(help(mylist.insert))

print(mylist)



def Print_Name():
     print("My name is Aniket")

def Print_Name(name):
     #Docsstring explains function  ''''''
     print("Your name is : {}".format(name))

Print_Name('Aniket')

def add_function(num1,num2):
     return num1 + num2

result = add_function(1,2)
print("Addition is : ",result)


def say_hello(name='Default'):
     print(f'Hello {name}')

say_hello()

def sum_numbers(num1,num2):
     print(num1+num2)

sum_numbers(10,20)
sum_numbers('10','20')


'''

'''Logic with python functions''' 

expression1 = 20 % 3
print(expression1)


def even_check(number):
    result = (number % 2 == 0)
    return result

result = even_check(3)
print(result)

def check_even_list(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else :
            pass

    return False

result = check_even_list([1,3,5])
print("Even list: ",result)


#print all even numbers from list

even_list = []

def Print_even(num_list1):
    for element in num_list1:
        if element % 2 == 0:
            even_list.append(element)
        else:
            pass
    return even_list

result = Print_even([1,2,3,4,5])
print(result)
#print(even_list)

result2 = Print_even([1,3,5])
print(even_list)

