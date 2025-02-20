import sys
import math
import statistics

if len(sys.argv) > 1:
	print('number of values:', len(sys.argv) - 1)
	numbers = [float(arg) for arg in sys.argv[1:]]
	print('Min:', min(numbers))
	print('Max:', max(numbers))
	print('Mean:', statistics.mean(numbers))
	print('SD:', statistics.stdev(numbers))
	print('Median:', statistics.median(numbers))
	
	mean = statistics.mean(numbers)
	stdev = statistics.stdev(numbers)
	
	print("\nZ-scores:")
	for num in numbers:
		z_score = (num - mean) / stdev
		print(f"Z-score for {num}: {z_score:.4f}")
	
	

	
	
	