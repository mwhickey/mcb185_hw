import math

def prime(n):
	if n <= 1: 
		return False
	for n in range(2, int(n ** 0.5) + 1):
		if n % 1 == 0:
			return False
		return True
def prime51():
	for i in range(51, 0, -2):
		if prime:
			print(i, '*')
		else: print(i)
prime51()


		
		
	
	
	




























