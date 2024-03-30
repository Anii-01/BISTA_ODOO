#Map---

def square(num):
    return num**2

my_nums = [1,2,3,4,5]
for item in map(square,my_nums):
    print(item)

print(list(map(square,my_nums)))


def addition(no1,no2):
    return no1+no2

mylist = ['a','b','c','d']
for item in map(addition,mylist,mylist):
    print(item)

#Filter---

def check_even(num):
     return num%2 == 0
my_nums = [1,2,3,4,5,6]
print(list(filter(check_even,my_nums)))

for n in filter(check_even,my_nums):
     print(n)


# lambda function
     

def square(num):
    result = num ** 2            # or return num**2
    return result

result = square(3)
print(result)

square2 = lambda num: num ** 2
result2 = square2(3)
print(result)

# lambda with map
result3 = list(map(lambda num:num**2,my_nums))
print(result3)

# lambda with filter
result4 = list(filter(lambda num: num%2==0,my_nums))
print(result4)

names = ("aniket","Shweta","nikhil")
result5 = list(map(lambda x:x[0],names))
print(result5)

result6 = list(map(lambda x:x[::-1],names))
print(result6)
