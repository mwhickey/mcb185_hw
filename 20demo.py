
import math

t = 1, 2
print(t)
print(type(t))

person = 'Steve', 21, 57891.50
print(person)

def midpoint(x1, y1, x2, y2):
	x = (x1 + x2) / 2
	y = (y1 + y2) / 2
	return x, y
print(midpoint(1, 2, 3, 4))
m = midpoint(1, 2, 3, 4)
print(m[0], m[1])

mx, my = midpoint(1, 2, 3, 4)
print(mx, my)

i = 0
while i < 10:
	print(i)
	i = i + 3
print('final value of i is', i)

for i in range(1, 10, 3):
	print(i)

for i in range(0, 5):
	print(i)

for i in range(5):
	print(i)
	
basket = 'milk', 'eggs', 'bread'
for thing in basket:
	print(thing)
	
for i in range(len(basket)):
	print(basket[i])
	
	
	
for i in range(7):
	if i % 2 == 0: print(i, 'is even')
	else: 	print(i, 'is odd')	
	
random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())

def montpi():
	inside_circle = 0
	total = 0
	while True:
		x = random.random()
		y = random.random()
		distance = math.sqrt(x**2 + y**2)
		if distance <= 1:
			inside_circle += 1	
		total += 1
		pi_estimate = 4 * (inside_circle / total)
		print(total, pi_estimate)
montpi()