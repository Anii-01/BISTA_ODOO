t = ('one',2)
print(t[0])
print(t[-1])
t = ('a','a','a','b')
print(t.count('a'))

print(t.index('a'))


myset = {1,2,3,4}
print(myset)
print(type(myset))

test_set = set("Aniket")
print(test_set)
print(type(test_set))


print(type(True))

x = open('test.txt','w')
x.write('Hello World .. i wrote something..')
x.close()