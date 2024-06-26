

class Fibonacci:

	n1 = 0;
	n2 = 1;
	n3 = 0;

	def __init__(self,n):
		self.no = n
		
		
	def Fib(self,n):
		
		print("Fibonacci series is : ")
		print(n1)
		print(n2)
		
		for i in range(2,n):
			n3 = n1 + n2
			print(n3)
			n1 = n2;
			n2 = n3;

n = int(input("Enter no : "))
obj = Fibonacci(n)
obj.Fib(n)

#10.30 - 11.30 
