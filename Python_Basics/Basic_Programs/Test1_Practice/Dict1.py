
mydict = { "first": "one",
          "second":"two","third":"three","4":"four","5":"Five",21:True , 21:True,21:'aniket'}

print(mydict)

print(mydict.values())
print(mydict.keys())
print(mydict.items())

mydict2 = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six'}

for k,v in mydict2.items():
    print(k,end=' ')
    #print(v,end=' ')

print("\nTuple unpacking : ")

my_tuple = ((1,2),(3,4),(5,6),(7,8))

for i,j in my_tuple:
    print(i)

print("list unpacking")

Mylist = [('a','b'),('b','c'),('d','e'),('f','g')]
print(Mylist)

for i,j in Mylist:
    print(i,end=' ')
    print(j)

set_s1 = {'a','s','d','f','g','e','f'}
print(set_s1)
print(type(set_s1))

