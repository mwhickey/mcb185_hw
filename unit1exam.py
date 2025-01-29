import math

def dist2(x1, y1, x2, y2):
	x_dist = x2 - x1
	y_dist = y2 - y1
	return math.sqrt(x_dist ** 2 + y_dist ** 2)
print(dist2(0, 0, 3, 4))

def harmonicmean(a, b, c, d): 
	n=4
	sum = (1/a) + (1/b) + (1/c) + (1/d)
	return n/sum
print(harmonicmean(5, 5, 7, 7))

def max4(a, b, c, d):
	if a >= b and a >= c and a >= d:
		return a
	elif b >= a and b >= c and b >= d:
		return b
	elif c >= a and c >= b and c >= d:
		return c
	else:
		return d
print(max4(2, 5, 9, 14))

def prob(n):
	if (n >= 0 and n <= 1):
		return True
	else: 
		return False
print(0.3)

