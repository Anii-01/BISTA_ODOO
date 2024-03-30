import random

#random numbers
print(random.randint(0,100))

#fix set of random number
random.seed(101)
a = random.randint(0,100)
print(a)

#-------------------
mylist = list(range(0,20))
print("Mylist : ",mylist)

#sample with replacement
print(random.choices(population=mylist,k=10))

#sample without replacement
print(random.sample(population=mylist,k=10))

#-------------------
print("Before shuffle Mylist: ",mylist)
random.shuffle(mylist)
print("After shuffle Mylist: ",mylist)

#----------------------

uniform_dist = random.uniform(a=0,b=100)
print(uniform_dist)

gaussion_dist = random.gauss(mu=0,sigma=1)
print(gaussion_dist)