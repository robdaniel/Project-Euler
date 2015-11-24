answer = 0
rem = 0
x = 0

for i in range(10,200000):
	result = 0
	x = i
	while x > 0:
		rem = x % 10
		result += pow(rem,5)
		x = x/10
	if result == i:
		print "%d" % result
		answer += result

print "Answer: %d" % answer