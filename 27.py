def isPrime(number):
	if number <= 1:
		return False
	elif number <= 3:
		return True
	elif (number % 2 == 0) or (number % 3 == 0):
		return False
	i = 5
	while (i*i) <= number:
		if (number % i == 0)or (number % (i + 2) == 0):
			return False
		i += 6
	return True


def quad(num, ax, bx):
	result = 0
	result = num*num + ax*num + bx
	return isPrime(result)

maxCons = [0, 0, 0]

for each in range(-999, 1000):
	for each2 in range(-999, 1000):
		active = True
		n = 0
		while active:
			if quad(n, each, each2):
				n += 1
			elif n > 0:
				if n > maxCons[0]:
					maxCons = [n, each, each2]
				active = False
			else:
				active = False

print "Product of coefficients is:", (maxCons[1]*maxCons[2])