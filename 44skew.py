import sequence
import sys

seq = ""

with open(sys.argv[1]) as fp:
	for line in fp:
		if line[0] != '>': 
			seq = seq + line
w = 1000
s = seq[:w]
for i in range(len(seq) -w + 1):
	s = s[1:] + seq[i + w + 1]
	print(i, sequence.gc_comp(s), sequence.gc_skew(s))



