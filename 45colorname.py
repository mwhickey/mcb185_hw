import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

def dtc(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return d

clcolor = [R, G, B]

with open(colorfile) as fp:
	mini = 768
	color = ""
	for line in fp:
		cols = line.split()
		cols[2] = cols[2].split(',')
		for i in [0,1,2]:
			cols[2][i] = int(cols[2][i])
		
		dist = dtc(clcolor, cols[2])
		if dist < mini: 
			mini = dist
			color = cols[0]
print(mini, color)
		


	
	
	
	
	
	

