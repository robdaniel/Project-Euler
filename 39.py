
def isTriangle(a, b, c):
	if ((a ** 2) + (b ** 2)) == (c ** 2):
		return True
	return False

results = [0 for each in range(0, 1000)]
high = 0

for p in range(1, 1000):
	for i in range(1,500):
		for j in range(i, 500):
			for k in range(j, 500):
				if isTriangle(i, j, k) and ((i + j + k) == p):
					results[p-1] += 1

for each in results:
	if each > high:
		high = each

print high