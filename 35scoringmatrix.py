import sys


def scorematrix(alphabet, match, mismatch):
	header = " " + " ".join(alphabet)
	print(header)

	for row in alphabet: 
		rowdata = [row]
		for col in alphabet:
			if row == col:
				rowdata.append(str(match))
			else: 
				rowdata.append(str(mismatch))
		print(" ".join(rowdata))

def main():
	if len(sys.argv) != 4:
		sys.exit(1)
	
	alphabet = sys.argv[1]
	try:
		match = int(sys.argv[2])
		mismatch = int(sys.argv[3])
	except error:
		sys.exit(1)
		
	scorematrix(alphabet, match, mismatch)

main()