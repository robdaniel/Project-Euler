
def isPrime(number):
	if number == 2 or number == 3: return True
	if number%2 == 0 or number < 2: return False
	for each in range(3, int(number**0.5) + 1, 2):
		if number % each == 0:
			return False
	return True

def isTruncatableLeftRight(number):
	length = len(str(number))
	for each in range(1, length+1):
		newNum = number % (10 ** each)
		if not isPrime(newNum):
			return False
	return True

def isTruncatableRightLeft(number):
	length = len(str(number))
	for each in range(0, length):
		newNum = number / (10 ** each)
		if not isPrime(newNum):
			return False
	return True

num = 11
result = 0
count = 0

while count < 11:
	if isPrime(num):
		if isTruncatableLeftRight(num) and isTruncatableRightLeft(num):
			result += num
			count += 1
	num += 1

print result