n = pow(2,1000)
num = n
rem = 0
total = 0

while num > 0:
	rem = num % 10
	num = num/10
	total += rem

print "Answer: %d" % total
