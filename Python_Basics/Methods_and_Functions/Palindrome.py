string = input("Enter the string: ")

def Chk_Palindrome(string):

    string = string.replace(' ','')
    print(string)
    rev_string = string[::-1]
    if(rev_string == string):
        print("It is palindrome!")
    else:
        print("It is not a palindrome!")

Chk_Palindrome(string)

