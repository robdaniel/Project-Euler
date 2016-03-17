from bitstring import BitArray

def ESieve(upperLimit):
	sieveBound = (upperLimit - 1) / 2
	upperSqrt = ((upperLimit ** 0.5) - 1) / 2

	PrimeBits = BitArray(sieveBound + 1)
	PrimeBits.set[1]

	for i in range(1, upperSqrt + 1):
		if PrimeBits[i]:
			for j in range((i * 2 * (i + 1)), sieveBound + 1, (2 * i + 1)):
				PrimeBits[j] = False

	numbers = [upperLimit / (math.loglp(upperLimit) - 1.08366)]
	numbers.append(2)

	for i in range(1, sieveBound + 1):
		if PrimeBits[i]:
			numbers.append(2 * i + 1)

	return numbers


def isPrime(number):
	if number == 2 or number == 3: return True
	if number%2 == 0 or number < 2: return False
	for each in range(3, int(number**0.5) + 1, 2):
		if number % each == 0:
			return False
	return True

def isPandigital(num):
	n = len(str(num))

	for i in range(1, n + 1):
		if str(i) not in str(num):
			return False
	return True

primes = []
primes = ESieve(987654321)
result = 0

for i in range((len(primes) - 1), -1, -1):
	if isPandigital(primes[i]):
		result = primes[i]
		break

# while not found:
# 	print start
# 	if isPandigital(start):
# 		if isPrime(start):
# 			print "Boobies"
# 			found = True
# 	start -= 1
