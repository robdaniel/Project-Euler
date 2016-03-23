import itertools
import math

# def is09Pandigital(num):
# 	n = len(str(num))
# 	if n!= 10:
# 		return False
# 	for i in range(0, n):
# 		if str(i) not in str(num):
# 			return False
# 	return True

def isSubString(number):
	n = number
	d234 = int(n[1]*100 + n[2]*10 + n[3])
	if d234 % 2 == 0:
		d345 = int(n[2]*100 + n[3]*10 + n[4])
		if d345 % 3 == 0:
			d456 = int(n[3]*100 + n[4]*10 + n[5])
			if d456 % 5 == 0:
				d567 = int(n[4]*100 + n[5]*10 + n[6])
				if d567 % 7 == 0:
					d678 = int(n[5]*100 + n[6]*10 + n[7])
					if d678 % 11 == 0:
						d789 = int(n[6]*100 + n[7]*10 + n[8])
						if d789 % 13 == 0:
							d8910 = int(n[7]*100 + n[8]*10 + n[9])
							if d8910 % 17 == 0:
								return True
	return False

def convToInt(Str):
	result = 0
	for each in range(9, -1, -1):
		result += (Str[9 - each] * math.pow(10, each))
	return int(result)

result = list(itertools.permutations([1,2,3,4,5,6,7,8,9,0]))
sumAll = 0

for num in result:
 	if isSubString(num):
 		sumAll += convToInt(num)
 		print convToInt(num)

print sumAll