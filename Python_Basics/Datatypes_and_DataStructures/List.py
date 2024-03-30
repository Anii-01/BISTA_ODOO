my_list = [1,2,3]
print(my_list)

my_list = ['STRING',100,23.2]
print(my_list)

print(len(my_list))

mylist = ['one','two','three']
print(mylist[0])
print(mylist[1])

print(mylist[1:])

another_list = ['four','five']

new_list = mylist + another_list
print(new_list)
#rint(mylist + another_list)

new_list[0] = 'ONE'    #List are mutable
print(new_list)
new_list.append(6)
print(new_list)

popped_item = new_list.pop()
new_list.pop(0)
print(new_list)
print(popped_item)

new_list = ['a','e','o','u','x','b','c']
num_list = [4,1,8,3]

new_list.sort()
print(new_list)

num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

