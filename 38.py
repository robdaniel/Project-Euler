import math

def is09Pandigital(num):
	n = len(str(num))
	if n != 9:
		return False
	for i in range(1, n+1):
		if str(i) not in str(num):
			return False
	return True

def prodConcat(number, List):
	result = []
	for each in List:
		result.append(str(number * each))
	answer = ''.join(result)
	return answer

maxPand = 0
temp = []

for num in range(0, 9999):
	if num < 10:
		temp = prodConcat(num, [1, 2, 3, 4, 5])
		if is09Pandigital(int(temp)):
			if temp > maxPand:
				maxPand = temp
	elif num < 34:
		temp = prodConcat(num, (1, 2, 3, 4))
		if is09Pandigital(int(temp)):
			if temp > maxPand:
				maxPand = temp
	elif num < 334:
		temp = prodConcat(num, (1, 2, 3))
		if is09Pandigital(int(temp)):
			if temp > maxPand:
				maxPand = temp
	else:
		temp = prodConcat(num, (1, 2))
		if is09Pandigital(int(temp)):
			if temp > maxPand:
				maxPand = temp

print "Max Pandigital is:", maxPand