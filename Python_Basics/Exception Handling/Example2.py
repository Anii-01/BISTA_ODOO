
try:
	k = 5//2
	print(k)

except ZeroDivisionError:
	print("Can't divide by zero")
	
else:
	print("in else , means no exception occured..")

finally:
	print('This is always executed')
