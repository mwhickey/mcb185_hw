def oligotemp(A, C, G, T):
	nt = A + C + G + T
	if nt <= 13:
		return (A + T) * 2 + (G + C) * 4
	else: 
		return 64.9 + 41 * (G + C - 16.4) / (A + T + G +C)
print(oligotemp(3, 2, 4, 3))

