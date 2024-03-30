def my_generator():
    for i in range(50):
        yield i

gen = my_generator()
print(next(gen))

print(next(gen))

print(next(gen))

gen2 = my_generator()
print(next(gen2))



