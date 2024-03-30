try:
    res = 190 / 0
except Exception as error:
    # handle the exception
    print("An exception occurred:", error)


try:
    # Code that may raise an exception
    1 / 0
except Exception as e:
    # Print the exception object
    print(e)

