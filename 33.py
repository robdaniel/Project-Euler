result = 0

for i in range(11,100):
	for j in range(10,100):
		if (i/10) == (j%10) and j%10 != 0:
			test1 = (i/10)/(j%10)
			test2 = i/j
			if test1 == test2:
				result *= j

print "Answer: %d" % result