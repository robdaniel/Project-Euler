pence = 200
coins = [200, 100, 50, 20, 10, 5, 2, 1]
combos = 0
multiply = 2
place = 0
curr = 0
count = 0

for each in coins:
	curr = each
	if curr == pence:
		combos += 1
	if curr < pence:
		while curr*multiply <= pence:
			curr = curr*multiply
			multiply += 1
		multiply = 2
		if curr == pence:
			combos += 1
		else:
			while place < 7:
				place += 1
				if curr + coins[place] == pence:
					combos += 1
				while curr + (coins[place])*multiply <= pence:
					curr = curr + coins[place]*multiply
					multiply += 1
				multiply = 2
				if curr == pence:
					combos += 1






				# place += 1
				# if curr + coins[place] == pence:
				# 	combos += 1
				# while curr + (coins[place])*multiply <= pence:
				# 	curr = curr + coins[place]*multiply
				# 	multiply += 1
				# multiply = 2
				# if curr == pence:
				# 	combos += 1
				# else:
				# 	place += 1
				# 	if curr + coins[place] == pence:
				# 		combos += 1
				# 	while curr + (coins[place])*multiply <= pence:
				# 		curr = curr + coins[place]*multiply
				# 		multiply += 1
				# 	multiply = 2
				# 	if curr == pence:
				# 		combos += 1
				# 	else:
				# 		place += 1
				# 		if curr + coins[place] == pence:
				# 			combos += 1
				# 		while curr + (coins[place])*multiply <= pence:
				# 			curr = curr + coins[place]*multiply
				# 			multiply += 1
				# 		multiply = 2
				# 		if curr == pence:
				# 			combos += 1
				# 		else:
				# 			place += 1
				# 			if curr + coins[place] == pence:
				# 				combos += 1
				# 			while curr + (coins[place])*multiply <= pence:
				# 				curr = curr + coins[place]*multiply
				# 				multiply += 1
				# 			multiply = 2
				# 			if curr == pence:
				# 				combos += 1
				# 			else:
				# 				place += 1
				# 				if curr + coins[place] == pence:
				# 					combos += 1
				# 				while curr + (coins[place])*multiply <= pence:
				# 					curr = curr + coins[place]*multiply
				# 					multiply += 1
				# 				multiply = 2
				# 				if curr == pence:
				# 					combos += 1
				# 				else:
				# 					place += 1
				# 					if curr + coins[place] == pence:
				# 						combos += 1
				# 					while curr + (coins[place])*multiply <= pence:
				# 						curr = curr + coins[place]*multiply
				# 						multiply += 1
				# 					multiply = 2
				# 					if curr == pence:
				# 						combos += 1
				# 					else:
				# 						place += 1
				# 						if curr + coins[place] == pence:
				# 							combos += 1
				# 						while curr + (coins[place])*multiply <= pence:
				# 							curr = curr + coins[place]*multiply
				# 							multiply += 1
				# 						multiply = 2
				# 						if curr == pence:
				# 							combos += 1
	count += 1
	place = count									

print combos


# def countCoinCombs(left, i, comb, add):
# 	if add: comb.append(add)
# 	if left == 0 or (i + 1) == len(denominations)