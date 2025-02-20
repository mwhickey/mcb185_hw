s = 'hello world'
print(s)

s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)
print('hey "dude" don\'t tell me what to do')

print(s.upper())
print(s)

print(s.replace('o', ''))
print(s.replace('o', '').replace('r', 'i'))

import math

print(f'{math.pi}')
print(f'{math.pi:.3f}')
print(f'{1e6 * math.pi:e}')
print(f'{"hello world":>20}')
print(f'{"hello world":.>20}')
print(f'{20:<10} {10}')

print('{} {:.3f}'.format('str.format', math.pi))

print('%s %.3f' % ('printf', math.pi))

seq = 'GAATTC'
print(seq[0], seq[1])
print(seq[-1])

for nt in seq:
	print(nt, end='')
print()

for i in range(len(seq)):
	print(i, seq[i])

s = 'ABCDEFGHIJ'
print(s[0:5])
print(s[0:8:2])

print(s[0:5], s[:5])
print(s[5:len(s)], s[5:])

print(s, s[::], s[::1], s[::-1])

dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3):
	codon = dna[i:i+3]
	print(i, codon)
	
tax = ('Homo', 'sapiens', 9606)
print(tax)
print(tax[0])
print(tax[::-1])

nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])
for i, nt in enumerate(nts):
	print(i, nt)
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])
for nt, name in zip(nts, names):
	print(nt, name)
for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)
	
nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)
nts.append('C')
print(nts)
last = nts.pop()
print(last)
nts.sort()
print(nts)
nts.sort(reverse = True)
print(nts)

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

items = list()
print(items)
items.append('eggs')
print(items)
stuff = []
stuff.append(3)
print(stuff)

alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)

text = 'good day	to you'
words = text.split()
print(words)

line = '1.41,2.72,3.14'
print(line.split(','))

s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

if 'A' in alph: print('yay')
if 'a' in alph: print('no')
print('index G?', alph.index('G'))
print('find G?', alph.find('G'))



print('-'.join(list('ABCDE'))[3:6])
#list ('ABCDE') -> converts string into a list of its characters
#'-'.join -> joins the elements of the list with a - in between each letter
# [3:6] -> slice that extracts characters 3-5 including dashes
# => -C-

def codonframe(seq):
	seqlength = len(seq)

	for frame in range(3):
		position = 1
	
		for i in range(frame, seqlength, 3):
			codon = seq[i:i+3]
			if len(codon) == 3:
				print(f"{position}\t{frame + 1}\t{codon}")
				position += 1

seq = 'ATGCTGTAA'
codonframe(seq)






