day = 3
last = 0
total = 0
# Day Variable
# 1 = Sunday
# 2 = Monday
# 3 = Tuesday
# 4 = Wednesday
# 5 = Thursday
# 6 = Friday
# 7 = Saturday

for y in range(1901,2001):
	for m in range(1,13):
		if m == 2:
			if y%4 == 0:
				if y%100 == 0:
					if y%400 == 0:
						last = 29
					else:
						last = 28
				else:
					last = 29
			else:
				last = 28
		elif m == 4 or m == 6 or m == 9 or m == 11:
			last = 30
		else:
			last = 31

		print "Last: %d" % last
		for d in range(1,last+1):
			if day == 1 and d == 1:
				total += 1
			print "%d, %d - %d - %d, %d" % (day,m,d,y,total)
			if day == 7:
				day = 1
			else:
				day += 1
			


print "Answer: %d" % total