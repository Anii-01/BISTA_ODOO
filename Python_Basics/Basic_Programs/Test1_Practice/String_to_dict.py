
string = "India is my country"

print(string)

print(tuple(string))
print(set(string))

for keys in string : 
    mydict = dict(keys,string)
print(mydict)


# git- github
# virtual env
#list and Dict
#dict and advance dict
#return dict
#list

#list comprehension
#set no updates

#string to dict

#notes - 
#repeating tuple in list
#tuple

#W3 school

# **** Codding conventions...!!!!!!

#microservices in python  - No







# using eval()

test_string = '{"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}'

print("The original string : " + str(test_string))

# using eval()
# convert dictionary string to dictionary
res = eval(test_string)

# print result
print("The converted dictionary : " + str(res))
