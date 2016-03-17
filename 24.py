from sets import Set

count = 0
final = [0 for each in range(0, 3628800)]
results = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

tempSet1 = Set([])
tempSet2 = Set([])
tempSet3 = Set([])
tempSet4 = Set([])
tempSet5 = Set([])
tempSet6 = Set([])
tempSet7 = Set([])
tempSet8 = Set([])
tempSet9 = Set([])

pool1 = Set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
pool2 = Set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
pool3 = Set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
pool4 = Set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
pool5 = Set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
pool6 = Set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
pool7 = Set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
pool8 = Set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
pool9 = Set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

for each in range(0,10):
	pool1.remove(each)
	tempSet1.add(each)
	results[0] = each
	for each2 in pool1:
		results[1] = each2
		tempSet2 = Set([each, each2])
		pool2.difference_update(tempSet2)
		for each3 in pool2:
			results[2] = each3
			tempSet3 = Set([each, each2, each3])
			pool3.difference_update(tempSet3)
			for each4 in pool3:
				results[3] = each4
				tempSet4 = Set([each, each2, each3, each4])
				pool4.difference_update(tempSet4)
				for each5 in pool4:
					results[4] = each5	
					tempSet5 = Set([each, each2, each3, each4, each5])
					pool5.difference_update(tempSet5)
					for each6 in pool5:
						results[5] = each6
						tempSet6 = Set([each, each2, each3, each4, each5, each6])
						pool6.difference_update(tempSet6)
						for each7 in pool6:
							results[6] = each7
							tempSet7 = Set([each, each2, each3, each4, each5, each6, each7])
							pool7.difference_update(tempSet7)
							for each8 in pool7:
								results[7] = each8
								tempSet8 = Set([each, each2, each3, each4, each5, each6, each7, each8])
								pool8.difference_update(tempSet8)
								for each9 in pool8:
									results[8] = each9
									tempSet9 = Set([each, each2, each3, each4, each5, each6, each7, each8])
									pool8.difference_update(tempSet8)
									for each10 in pool9:
										results[9] = each10
										result = int(''.join(map(str, results)))
										final[count] = result
										count += 1
										if count == 1000000:
											print result
									pool9.update(tempSet9)
								pool8.update(tempSet8)
							pool7.update(tempSet7)
						pool6.update(tempSet6)
					pool5.update(tempSet5)
				pool4.update(tempSet4)
			pool3.update(tempSet3)
		pool2.update(tempSet2)
	pool1.update(tempSet1)

