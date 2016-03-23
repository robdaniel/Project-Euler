import math

def isPentagonal(number):
	test = (math.sqrt(1 + (24 * number)) + 1) / 6
	if test % 1 == 0:
		return True
	else:
		return False

found = False
n = 1

while not found:
	p = n * (3 * n - 1) / 2
	for n2 in range(n, 0, -1):
		p2 = n2 * (3 * n2 - 1) / 2
		if isPentagonal(p - p2) and isPentagonal(p + p2):
			D = p - p2
			found = True
			break
	n += 1

print "k =", n, ", j =", n2
print "D =", D