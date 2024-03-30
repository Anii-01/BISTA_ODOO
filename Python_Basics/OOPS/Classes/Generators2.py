def my_generator():
    for i in range(50):
        yield i

gen = my_generator()

# Store yielded values in a list
values = list(gen)

# Iterate over the list in reverse
for value in reversed(values):
    print(value)

