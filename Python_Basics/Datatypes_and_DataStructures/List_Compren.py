
mystring = 'hello'

mylist = []

for letter in mystring:
    mylist.append(letter)

print(mylist)

string = 'Aniket'
mylist = [element for element in string]
print(mylist)

mylist = [element*2 for element in string]
print(mylist)

mylist2 = [1,2,3,4,5,6,7,8,9]
mylist2 = [x for x in mylist2 if x%2==0]
print(mylist2)

mylist2 = [x for x in mylist2 if x%2!=0]
print(mylist2)


new_mylist2 = [x for x in range(0,11) if x%2==0]
print(new_mylist2)

#very complecated to uderstand..
results = [x if x%2 == 0 else 'ODD' for x in range(0,11)]
print(results)

mylist = []

for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)

print(mylist)

mylist11 = [x*y for x in [2,4,6] for y in [100,200,300]]
print(mylist11)


