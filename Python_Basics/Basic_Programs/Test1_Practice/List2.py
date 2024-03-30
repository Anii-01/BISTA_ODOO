list = [1,2,3]

list.append(4)
print(list)

print(list.count(10))

x = [1,2,3]
x.append([4,5])        #whole interable
print(x)

x = [1,2,3]
x.extend([4,5])        #elements individually
print(x)

print(list.index(3))
list.insert(2,"inserted")
print(list)

#popped_ele = list.pop(2)
#print(popped_ele)

list.remove("inserted")                 #remove only first occurance
print(list)

list.reverse()                          #permently affected inplace
print(list)

list.sort()                             #inplace sort
print(list)


