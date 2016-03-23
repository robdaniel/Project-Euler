import itertools

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

pans = []
maxPrime = 0

pans.append(list(itertools.permutations('12')))
pans.append(list(itertools.permutations('123')))
pans.append(list(itertools.permutations('1234')))
pans.append(list(itertools.permutations('12345')))
pans.append(list(itertools.permutations('123456')))
pans.append(list(itertools.permutations('1234567')))
pans.append(list(itertools.permutations('12345678')))
pans.append(list(itertools.permutations('123456789')))

for each in pans:
	for each2 in each:
		result = ''.join(each2)
		num = int(result)
		if isPrime(num) and (num > maxPrime):
			maxPrime = num

print maxPrime