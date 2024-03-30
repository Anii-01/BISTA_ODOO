
'''
number = 123
rev = 0

while(number != 0):

    digit = number % 10
    print(digit)
    rev = (rev * 10)+ digit
    number = number // 10

print(rev)

'''

number = 123

string_no = str(number)
print(string_no)

mylist = list(string_no)
print(mylist)
mylist.reverse()
print(mylist)

string_no = string_no[::-1]
print(string_no)

print(type(string_no))
rev_no = int(string_no) 
print(rev_no)
print(type(rev_no))


x = -12345
String_no = str(x)
Rev_String = String_no[::-1]
Rev_no = int(Rev_String)

print(Rev_no)


        