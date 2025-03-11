import gzip
import sys

with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		if line[0] == '#': continue
		words = line.split()
		if words[2] != 'CDS': continue
		beg = int(words[3])
		end = int(words[4])
		print(end - beg + 1)
		

'''
import sys

file path = sys.argv[1]
fp = open(filepath)

for line in fp: 
	cols = line.split()
	print(cols[0])


Practice Problem: Average exon length

import gzip
import sys


filepath = sys.argv[1]
fp = gzip.open(filepath, 'rt')

#Inititalization Step

total = 0
num_exons = 0

# loop
for line in fp: 
	cols = line.split()
	if cols[2] == 'exon': 
		beg = int(cols[3])
		end = int(cols[4])
		total += end - beg + 1
		num_exons += 1
print(total / num_exons)


Another way to start program

filepath = sys.argv[1]

exons = 0
total = 0
with gzip.open(filepath, 'rt') as fp:
	for line in fp:
		f = line.split()
		if f[2] != 'exon': continue
		beg = int(f[3])
		end = int(f[4])
		total += end - beg + 1
		exons += 1
print(total/exons)


FASTA files

import gzip
import sys
import ____

filepath = sys.argv[1]
for defline, seq in mcb185.read_fasta(filepath):







