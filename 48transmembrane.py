


# alpha helices do not contain proline(P); signal peptide / transmembrane regions
# signal peptide: 8 aa long, average KD >= 2.5, first 30 aa
# transmembrane region: 11 aa long, average KD >= 2/0, after 30 aa
kdh = {
	'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5,
	'M':  1.9, 'A':  1.8, 'G': -0.4, 'T': -0.7, 'S': -0.8,
	'W': -0.9, 'Y': -1.3, 'P': -1.6, 'H': -3.2, 'E': -3.5,
	'Q': -3.5, 'D': -3.5, 'K': -3.9, 'N': -3.5, 'R': -4.5,
}
def hydropathy(seq):
	s = 0
	for aa in seq:
		s += kdh[aa]
	return s / len(seq)