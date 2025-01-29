import math

def qual2err(symbol):
	if len(symbol) != 1:
		return None
	ascii_value = ord(symbol)
	if not (33 <= ascii_value <= 126):
		return None
	phred_score = ascii_value - 33
	error_rate = 10 ** (-phred_score / 10)
	return error_rate
	
print(qual2err('A'))


def err2qual(er):
	if not (0 <= er <= 1):
		return None
	phred_score = -10 * math.log10(er)
	ascii_value = int(phred_score) + 33
	if 33 <= ascii_value <= 126:
		return chr(ascii_value)
	else: 
		return None
print(err2qual(0.001))



