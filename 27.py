import math

n = 0
a = 0
b = 0
stop = False

def prime(number):
	i = 2
	factors = []
	for i in range(2,int(sqrt(number)):
		if number%2 == 0:
			factors.append(i)
			factors.append(number/i)

			for k in range(0,2):
				isPrime = True
				for j in range(2,int(sqrt(factors[k]))):
					if factors[k]%j == 0:
						isPrime = False
						break
	return isPrime

def test(num, ax, bx):
	result = 0
	truth = False
	result = num*num + ax*num + bx
	truth = prime(result)
	return truth

while not stop:
	

