def addToDecimal(number, n):
	n = map(int, str(n))
	number.extend(n)
	return number

irrDec = []
x = 1

while len(irrDec) < 1000000:
	irrDec = addToDecimal(irrDec, x)
	x += 1

result = irrDec[0] * irrDec[9] * irrDec[99] * irrDec[999] * irrDec[9999] * irrDec[99999] * irrDec[999999]

print result