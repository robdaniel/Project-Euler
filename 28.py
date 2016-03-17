final = [[0 for item in range(0, 1001)] for item2 in range(0, 1001)]


s1 = 500
s2 = 500

final[s1][s2] = 1

count = 1
count2 = 2
count3 = 1000
total = 0
total1 = 0
total2 = 0

while count < 1002:
	
	if count == 1001:
		for finish in range(0, count - 1):
			s2 +=1
			final[s1][s2] = count2
			count2 += 1
		break

	for east in range(0, count):
		s2 += 1
		final[s1][s2] = count2
		count2 += 1

	for south in range(0, count):
		s1 += 1
		final[s1][s2] = count2
		count2 += 1

	count += 1

	if count == 1001:
		for finish in range(0, count - 1):
			s2 +=1
			final[s1][s2] = count2
			count2 += 1
		break

	for west in range(0, count):
		s2 -= 1
		final[s1][s2] = count2
		count2 += 1

	for north in range(0, count):
		s1 -= 1
		final[s1][s2] = count2
		count2 += 1

	count +=1

for each in range(0, 1001):
	total1 += final[each][each]

for each2 in range(0, 1001):
	total2 += final[count3][each2]
	count3 -= 1

total = total1 + total2 - 1

print total




