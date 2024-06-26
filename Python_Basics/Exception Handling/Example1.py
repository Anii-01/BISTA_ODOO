print("Before try!")

try:
    print("In try block..")
    def add(n01, n02):
        result = n01 + n02
        print("The result is : ", result)

    add(5, 'a')

except Exception as e:
    print("In except block..")
    print(e)

else:
    print("Hey, it looks like you aren't adding correctly")

finally:
    print("In finally block..")
