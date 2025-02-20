import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])
number = 0

for i in range(trials):
	bday = [random.randint(0, days - 1) for _ in range(people)]
	if len(bday) != len(set(bday)):
		number += 1
prob = number / trials
print(prob)


