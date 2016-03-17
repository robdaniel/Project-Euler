def findFactorial(number):
	if number == 0:
		return 1
	elif number == 1:
		return 1
	elif number == 2:
		return 2
	else:
		return (number * findFactorial(number-1))

num = []
final = 0

for each in range(10, 2540161):
	length = len(str(each))
	num = map(int, str(each))
	numSum = 0
	for each2 in range(0, length):
		numSum += findFactorial(num[each2])
	if numSum == each:
		final += each

print final