

from random import shuffle

example = [1,2,3,4,5,6,7,8,9]
result = shuffle(example)
#print(result)
#print("Without function:",example)


def shuffle_list(my_list):
    shuffle(my_list)
    return my_list

result = shuffle_list(example)
#print("With function:",result)

# ----

mylist = ['','O','']
shuffle_list(mylist)
#print(mylist)

def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0, 1, 0r 2 - ")
    return int(guess)

myindex = player_guess()
#print("My index is : ",myindex)


def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print("Correct!")
    else:
        print("Wrong guess!")
        print(mylist)

#initial list
mylist = [' ','O',' ']     
#shuffle list
mixedup_list = shuffle_list(mylist)
#user guess
guess = player_guess()
#check guess
check_guess(mixedup_list,guess)




