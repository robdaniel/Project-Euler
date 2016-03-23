i = 100
n = 1
rem = 0
total = 0
while i > 0:
	n *= i
	i -= 1

num = n
while num > 0:
	rem = num % 10
	num = num/10
	total += rem

print "Answer: %d" % total