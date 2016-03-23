def is09Pandigital(num):
	n = len(str(num))
	if n != 9:
		return False
	for i in range(1, n+1):
		if str(i) not in str(num):
			return False
	return True

answer = []
result = 0

for each in range(1, 9999):
	for each2 in range(1, 9999/each):
		prod = each * each2
		length = str(each) + str(each2) + str(prod)
		if len(length) == 9:
			if is09Pandigital(int(length)):
				if prod not in answer:
					answer.append(prod)

for answers in answer:
	result += answers

print result