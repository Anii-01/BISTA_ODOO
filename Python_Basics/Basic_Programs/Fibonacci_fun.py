
def Fibonacci(n):
	
	no1 = 0;
	no2 = 1;
	no3 = 0;
	
	print("Fibonacci series is :" )
	print(no1)
	print(no2)
	
	for i in range(2,n):
		no3 = no1 + no2
		print(no3)
		no1 = no2;
		no2 = no3;

n = int(input("Enter the no: "))
Fibonacci(n);
		
		
	


