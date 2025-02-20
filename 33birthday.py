import random

shared = 0
trials = 10000
days = 365
students = 23

for t in range(trials):
#make empty calendar
	calendar = []
	for i in range(days):
		calendar.append(0)
	
# add student birthdays	
	for i in range(students):
		bday = random.randint(0, days-1)
		calendar[bday] += 1

#check for shared birthdays
	collision = False
	for day in range(len(calendar)):
		if calendar[day] > 1: 
			shared += 1
			break

print(shared/trials)
