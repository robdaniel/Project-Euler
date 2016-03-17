count = 0

def isPrime(number):
	if number == 2 or number == 3: return True
	if number%2 == 0 or number < 2: return False
	for each in range(3, int(number**0.5) + 1, 2):
		if number % each == 0:
			return False
	return True

def isCircularPrime(number):
	length = len(str(number))
	if length == 1 and isPrime(number):
		return True
	newNum = number
	for each in range(0, length):
		temp = newNum % 10
		newNum = newNum/10
		newNum += (temp*(10 ** (length-1)))
		if not isPrime(newNum):
			return False
	return True

for each in range(1, 1000000):
	if isCircularPrime(each):
		count += 1

print count