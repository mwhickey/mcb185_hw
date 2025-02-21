import sys
import math

#creates list "numbers" which coverts command line numbers into floating point numbers
numbers = [float(arg) for arg in sys.argv[1:]]
if len(numbers) > 0:
	count = len(numbers)
	mini = min(numbers)
	maxi = max(numbers)
	mean = sum(numbers) / count
	variance = sum((num-mean)**2 for num in numbers) / count
	stdev = math.sqrt(variance)
	numbers.sort()
	if count % 2 == 0:
		median = (numbers[count // 2-1] + numbers[count // 2]) / 2
	else:
		median = numbers[count // 2]
	zscores = [(num-mean) / stdev for num in numbers] if stdev != 0 else [0]*count
	print(f"Number of values: {count}")
	print(f"Minimum: {mini}")
	print(f"Maximum: {maxi}")
	print(f"Mean: {mean}")
	print(f"Standard Deviation: {stdev}")
	print(f"Median: {median}")
	for num, z in zip(numbers, zscores):
		print(f"Value: {num} Z-score: {z:.4f}")


	
	

	
	
	