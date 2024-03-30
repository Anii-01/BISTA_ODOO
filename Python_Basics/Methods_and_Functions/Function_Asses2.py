import math as np
PI = np.pi
#1

def Cal_Vol(r):
    return ((4/3)*(PI)*(r**3))

result = Cal_Vol(2)
print("with normal fun:",result)

result = lambda r: ((4/3)*(3.14)*(r*r*r))
print("with lambda fun:",result(2))



#2

def Check_Range(num,low,high):
    for i in range(low,high):
        if ((num>=low) and (num<=high+1)):
            return True
    return False

result = Check_Range(10,0,10)
if result == True:
    print("Number is present in range")
else:
    print('Number is not present in range')

#3
# Count of capital and small

def Count_Case(string):
    index = 0
    Capital_Cnt = 0
    Small_Cnt = 0
    while(index < len(string)):
        if(string[index] >= 'A' and string[index] <= 'Z'):
            Capital_Cnt = Capital_Cnt + 1
        if(string[index] >= 'a' and string[index] <= 'z'):
           Small_Cnt = Small_Cnt + 1
        
        index = index + 1
    
    return (Capital_Cnt,Small_Cnt)

result = Count_Case('Aniket13')
print(result)

# or

def Count_Case2(string):
    index = 0
    Capital_Cnt = 0
    Small_Cnt = 0
    while(index < len(string)):
        if(string[index].isupper()):
            Capital_Cnt = Capital_Cnt + 1
        if(string[index].islower()):
           Small_Cnt = Small_Cnt + 1
        else:
            pass
    
        index = index + 1
    
    return (Capital_Cnt,Small_Cnt)

result2 = Count_Case2('AniketPhand')
print(result2)
        

#4

my_List = [1,1,1,2,3,3,4,5,6,1,2,3,4]
def unique_list(lst):
    return list(set(lst))

unique_list = unique_list(my_List)
print(unique_list)


import string

# pangram

def ispangram(str1 , alphabet=string.ascii_lowercase):

    alphaset = set(alphabet)
    str1 = str1.replace(' ','')
    str1 = str1.lower()
    str1 = set(str1)
    return str1 == alphaset

print(ispangram("Aniket"))
print(ispangram("The quick brown fox jumps over the lazy dog"))

print(string.ascii_lowercase)
