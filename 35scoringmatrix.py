import sys
	
	
base = sys.argv[1]
match = sys.argv[2]
mismatch = sys.argv[3]

	
print("   " + "  ".join(base))

for row in base: 
	rowlist = []
	rowlist.append(row)
	for col in base:
		if row == col:
			rowlist.append(str(match))
		else: 
			rowlist.append(str(mismatch))
	print(" ".join(rowlist))


