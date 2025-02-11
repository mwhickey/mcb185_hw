

def is_prime(n):
	for den in range(2, n//2):
		if n % den == 0: return False
	return True
def prime51():
	for n in range(51, 0, -2):
		if is_prime(n):
			print(n, '*')
		else: print(n)
prime51()

	
	
	




























