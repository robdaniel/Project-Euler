result = 0
combs = []

for a in range(2,101):
	for b in range(2,101):
		result = pow(a,b)
		combs.append(result)

combs = list(set(combs))
combs.sort()

#for i in range(0,int(len(combs))):
#	print "%d" % combs[i]

print "Answer: %d" % int(len(combs))