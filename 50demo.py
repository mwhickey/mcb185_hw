import random
import sys

names = []
vals = []
with open(sys.argv[1]) as fp:
	for line in fp:
		name, val = line.split()
		names.append(name)
		vals.append(val)






'''
for i in range(1000000):
	name = random.choices('ABCDEFGHIJKLMNOP', k=7)
	name = ''.join(name)
	print(name)
	sys.exit()
'''