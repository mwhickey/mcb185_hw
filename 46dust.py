import sys
import mcb185
import math

w = int(sys.argv[2])
ent = float(sys.argv[3])


def entropy(w):
	a = w.count('A') / len(w)
	c = w.count('C') / len(w)
	g = w.count('G') / len(w)
	t = w.count('T') / len(w)
	h = 0
	if a != 0: h += a * math.log2(a)
	if c != 0: h += c * math.log2(c)
	if g != 0: h += g * math.log2(g)
	if t != 0: h += t * math.log2(t)
	return -h

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	mask = list(seq)
	for i in range(len(seq) - w + 1):
		win = seq[i: i + w]
		if entropy(win) < ent:
			for j in range(i, i + w):
				mask[j] = 'N'
	print('>',defline,sep='')
	print(''.join(mask))
	
	
	