from collections import Counter

mylist = [1,1,1,1,1,2,2,2,3,3,3,3,4,4,4,3,3,]

print(Counter(mylist))
#counter is dict subclass

string = "AniketAniket"
print(Counter(string))

mylist2 = ['a','a',1,2,3,4,2,1,2,1,1]
print(Counter(mylist2))

#Counter()
string2 = "India is my country , India is my country"
string2 = string2.split()
Counter(string2)

#most_common()
string3 = 'AAAAAAAAABBBBBBccccdfsfsfsfdfsf'
c = Counter(string3)
print(c.most_common(3))             

#-----------------------------------------------------------------
from collections import defaultdict

d = {'a':10}
print(d['a'])

#print(d['wrong'])

d = defaultdict(lambda: 0)
d['correct'] = 100
print(d['WRONG KEY!'])
print(d)

#--------


mytuple = (10,20,30)

print(mytuple[0])

#index remembering is difficult for large tuples
from collections import namedtuple

Dog = namedtuple('Dog',['age','breed','name'])
sammy = Dog(age=5,breed='Husky',name='Sam')
print(type(sammy))
print(sammy)
print(sammy.age)
print(sammy.breed)
print(sammy[0])







        
