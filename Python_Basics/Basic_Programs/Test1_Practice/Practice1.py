
#list comprehension

name = ["aniket","nikhil","ram","sham"]
print(name)

newList = []

print(type(name))

for student in name :
    if 'a' in student:
        newList.append(student)
    else:
        pass
print(newList)

newList2 = [student for student in name if 'a' in student]
print(newList2)

#------------------------

#advance string : 
s = ' '

print(s.capitalize())
print(s.isspace())

s1 = 'hi\timlo'
print(s1.partition('i'))

print(s1)
print(s1.expandtabs(20))

