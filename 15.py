
latticeList = [[0 for x in range(21)] for x in range(21)]

for each in range(0,21):
	latticeList[0][each] = 1

for each in range(1,21):
	latticeList[each][0] = 1

for each in range(1,21):
	for each2 in range(1,21):
		latticeList[each][each2] = latticeList[each-1][each2] + latticeList[each][each2-1]

print latticeList[20][20]