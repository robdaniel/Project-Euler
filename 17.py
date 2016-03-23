words = [	["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"],
			["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"],
			["hundred"],
			["thousand"]
		]

letterCount = 0

for a in words[0]:
	letterCount += len(a)

for b in words[1]:
	letterCount += len(b)
	for c in range(0, 9):
		letterCount += len(b) + len(words[0][c])

for d in words[2]:
	for e in range(0, 9):
		letterCount += len(words[0][e]) + len(d)
		for f in words[0]:
			letterCount += len(words[0][e]) + len(d) + 3 + len(f)
		for g in words[1]:
			letterCount += len(words[0][e]) + len(d) + 3 + len(g)
			for h in range(0, 9):
				letterCount += len(words[0][e]) + len(d) + 3 + len(g) + len(words[0][h])

letterCount += 11

print "Total count is", letterCount