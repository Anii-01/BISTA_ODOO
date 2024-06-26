mylist = [1,2,3,4,5,6,7,8,9]
for number in mylist:
    print(number) 

for num in mylist:
    if(num % 2 ) == 0:
        print(num)

    mystring = "Hello world"

    for letter in mystring:
        print(letter)

print('\n')

tup = (1,2,3,4,5)

for item in tup:
    print(item)

print('\n')

mylist = [(1,2),(3,4),(5,6),(7,8)]
print(len(mylist))

for item in mylist:
    print(item)

print('\n')

#tuple unpacking

mylist = [(1,2),(3,4),(5,6),(7,8)]
print(len(mylist))

for a,b in mylist:
    print(a,end='')

print('\n')

for a,b in mylist:
    print(b,end='')

print('\n')

for a,b in mylist:
    print(a,end='')
    print(b,end='')

print('\n')

# Dictionary

d = {'k1':1, 'k2':2, 'k3':3}

for key,value in d.items():
    print(key)


str = 'Aniket'
for i in range(len(str)):
    #print(i)
    print(str[i],end='')