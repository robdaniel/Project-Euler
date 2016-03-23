pence = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]

combos = []

for each in range(0, pence + 1):
	combos.append(0)

combos[0] = 1

for i in range(0, len(coins)):
	for j in range(coins[i], pence+1):
		combos[j] += combos[j - coins[i]]

print combos[pence]