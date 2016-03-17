def proper_divs2(n):
	return {x for x in range(1, (n+1) // 2 + 1) if n % x == 0 and n != x}

mylist = [list(proper_divs2(n)) for n in range(1, 28112)]
abundant = []
abundantSum = []
temp = []
number = 1
results = []

for each in mylist:
	if (sum(each) > number):
		abundant.append(number)
	number += 1

for i in range(0, len(abundant)):
	for j in range(i, len(abundant)):
		aSum = abundant[i] + abundant[j]
		if aSum < 28124:
			abundantSum.append(aSum)

sortedSum = sorted(list(set(abundantSum)))

for each in range(1,28124):
	results.append(each)

results = set(results)

results.difference_update(sortedSum)

results = list(results)

print sum(results)