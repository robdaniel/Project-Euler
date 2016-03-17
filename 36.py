def isPalindromic(number):
	num = map(int, str(number))
	length = len(num)
	temp = length/2
	for each in range(0, temp):
		if num[each] != num[length - 1 - each]:
			return False
	return True

def base10ToBase2(number):
	temp = map(str, bin(number))
	temp.remove("0")
	temp.remove("b")
	temp = int(''.join(temp))
	return temp

results = 0

for each in range(1, 1000000):
	if isPalindromic(each) and isPalindromic(base10ToBase2(each)):
		results += each

print results