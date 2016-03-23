import math

def isTriangle(a, b, c):
	if ((a**2) + (b**2) == (c**2)):
		return True
	return False

maxCount = [0, 0]

for p in range(1, 1001):
	count = 0
	for a in range(1, p/2):
		for b in range(a, p/2):
			c = a**2 + b**2
			c = math.sqrt(c)
			if isTriangle(a, b, c):
				if ((a + b + c) == p):
					count += 1
	if count > maxCount[0]:
		maxCount = [count, p]

print "P =", maxCount[1]