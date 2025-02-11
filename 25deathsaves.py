import math
import random

trials = 1000000
die = 0
stable = 0
revive = 0
for i in range(trials):
	fail = 0
	success = 0
	for i in range(5): 
		r = random.randint(1, 20)
		if r == 1: fail += 2
		elif r <= 9: fail += 1
		elif r <= 19: success += 1
		else: 
			revive += 1
			break
		if success == 3: 
			stable +=1
			break
		if fail >= 3:
			die += 1
			break
dieprob = die / trials
stableprob = stable / trials
reviveprob = revive / trials
print('Probability of dying', dieprob)
print('Probability of stablizing', stableprob)
print('Probability of reviving', reviveprob)
