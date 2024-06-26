try:
    f = open('testfile','r')               #'w' mode - no error
    f.write("Write a test line")

except TypeError:
    print("There was a type error!")

#except OSError:
    #print("Hey you have an OS Error")

except Exception as e:
    print("All other exceptions!")
    print(e)
finally:
    print("I always run")
