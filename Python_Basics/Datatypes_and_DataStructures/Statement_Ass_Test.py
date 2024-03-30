#1
#Print words start with 's':

st = 'Print only the words that words start with s in this sentence'

word_list = st.split(' ')

for word in word_list:
    if word[0:1] == 's' or word[0] == 'S':    #word[0].lower()
        print(word)
    
#2

for number in range(0,11):
    if number % 2 == 0:
        print(number)


#3
        
mylist = [number for number in range(1,51) if number%3 == 0]
print(mylist)


#4
st = "Print every word in this sentence that has an even number of letters"
st = st.split(' ')

for word in st:
    if len(word) % 2 == 0:
        print(word + ' has even length')


#5

for number in range(1,101):
    if (number % 3 == 0) and (number % 5 == 0):
        print("Fizz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
    

#6
#Use list Comprehension to create a list of the first letters of every word in the string below
        
st = 'Create a list of the first letters of every word in this string'

mylist1  = st.split(' ')

mylist1 = [letter[0:1] for letter in mylist1]
print(mylist1)


