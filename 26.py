import math

decimals = []
temp = []
maxRec = [0, 0, 0]

for each in range(999, 1, -1):
	result = (1.0 / (each * 1.0))
	result = str(result)
	result = result[2:]
	result = int(result)
	temp = [each, result]
	decimals.append(temp)
	remainders = []
	remainders.append((result % each))
	length = 1
	for num in range(1, each):
		temp2 = ((10*remainders[num - 1]) % each)
		if temp2 not in remainders:
			remainders.append(temp2)
			length += 1
		elif temp2 in remainders:
			break
	if length > maxRec[0]:
		maxRec = [length, each, result]

print "D =", maxRec[1]