i = 0
b = 0
props = 0

def d(n):
	total = 0
	for x in range (1,n):
		if n%x == 0:
			total += x
	return total

for a in range(1,10000):
	b = d(a)
	i = d(b)
	if i == a and a != b:
		props += a

print "Answer: %d" % props