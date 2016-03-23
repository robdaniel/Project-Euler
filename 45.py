import math

def isTriangular(num):
	test = (math.sqrt(1 + (8 * number)) - 1) / 2
	if test % 1 == 0:
		return True
	else:
		return False

def isPentagonal(number):
	test = (math.sqrt(1 + (24 * number)) + 1) / 6
	if test % 1 == 0:
		return True
	else:
		return False

def isHexagonal(number):
	test = (math.sqrt(1 + (8 * number)) + 1) / 4
	if test % 1 == 0:
		return True
	else:
		return False

found = False
n = 286

while not found:
	t = n * (n + 1) / 2
	if isPentagonal(t) and isHexagonal(t):
		print t
		found = True
		
	n += 1