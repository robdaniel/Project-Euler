result = 1
numerator = 1
denom = 1

for i in range(1, 10):
	for each in range(2,10):
		for each2 in range(1,each):
			if ((each2 * 10 + i) * each) == ((i * 10 + each) * each2):
				denom *= each
				numerator *= each2
print numerator, "/", denom, "->", denom/numerator
