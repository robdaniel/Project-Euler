import csv

letters = [	["A", 1], ["B", 2], ["C", 3], ["D", 4], ["E", 5], ["F", 6], 
		["G", 7], ["H", 8], ["I", 9], ["J", 10], ["K", 11], 
		["L", 12], ["M", 13], ["N", 14], ["O", 15], ["P", 16], 
		["Q", 17], ["R", 18], ["S", 19], ["T", 20], ["U", 21], 
		["V", 22], ["W", 23], ["X", 24], ["Y", 25], ["Z", 26]]

f1 = file('words2.csv', 'rU')
c1 = csv.reader(f1)

count = 0

def T(number):
	Tn = 0.5*number*(number + 1)
	return Tn

def findLetterValue(letter):
	found = False
	for each in letters:
		if each[0] == letter:
			return int(each[1])

def findWordValue(word):
	wordValue = 0
	for each in word:
		wordValue += findLetterValue(each)
	return wordValue

def isTriangular(value):
	for each in range(1, 1000000):
		t = T(each)
		if t == value:
			return True
		elif t > value:
			return False

masterlist = list(c1)

for masterlist2 in masterlist:
	for each in masterlist2:
		wordValue = findWordValue(each)
		if isTriangular(wordValue):
			print wordValue
			count += 1

print count