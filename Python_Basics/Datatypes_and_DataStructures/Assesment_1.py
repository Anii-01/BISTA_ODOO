import math

#1

exp1 = (25 * 4) + 0.25
#exp2 = (200 / 2) + 0.25
exp2 = (60+(10**2)/4*7)-134.75

print(exp1)
print(exp2)

#2

exp3 = 4 * (6 + 5)
print(exp3)

exp4 = 4 * 6 + 5
print(exp4)

exp5 = 4 + 6 * 5
print(exp5)

#3

exp6 = 3 + 1.5 + 4
print(exp6)
print(type(exp6))       #implicit type conversion or type conversion 

#4
#square and square root

no1 = 5
square = no1 ** 2
print(square)

sqaure_root = math.sqrt(no1)
print(sqaure_root)

#5
#Strings

s = 'hello'
print(s[1])

#6
#reverse string using slicing

s = 'hello'
print(s[::-1])

#7
#print o
print(s[4:5:1])

last_element = s[-1]
print(last_element)

#8
list1 = [0,0,0]
print(list1)


list2 = [[0,0,0,],1,2,3,]
print(list2[0])

#9
#reassign 'hello'
list3 = [1,2,[3,4,'hello']]
list3[2][2] = "goodbye"
print(list3)

#10
#sort list
list4 = [5,3,4,6,1]
list4.sort()
print('Sorted list is : ',list4)

#Dictionaries
#grab hello

d = {'simple_key': 'hello'}
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

d = {'k1' :[{'next_key':['this is deep',['hello']]}]}
print(d['k1'])

#print(d[k1][0])
print(d['k1'][0]['next_key'][1][0])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

my_dict = {'b': 2, 'a': 1, 'c': 3}
sorted_keys = sorted(my_dict.keys())
for key in sorted_keys:
    print(key, my_dict[key])


#tuple
    
tuple1 = ("aniket",21,"Pune")
print(tuple1)

#sets

list5 = [1,2,2,33,4,4,11,22,3,3,2]
set_s1 = set(list5)
print(set_s1)


#Comparision Operators

# last question

l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

result = l_one[2][0] >= l_two[2]['k1']
print(result)




