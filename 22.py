import csv

letters = [	["A", 1], ["B", 2], ["C", 3], ["D", 4], ["E", 5], ["F", 6], 
		["G", 7], ["H", 8], ["I", 9], ["J", 10], ["K", 11], 
		["L", 12], ["M", 13], ["N", 14], ["O", 15], ["P", 16], 
		["Q", 17], ["R", 18], ["S", 19], ["T", 20], ["U", 21], 
		["V", 22], ["W", 23], ["X", 24], ["Y", 25], ["Z", 26]]

def findValue(name):
	value = 0
	for letter in name:
		for each in letters:
			if letter == each[0]:
				value += each[1]
	return value

f1 = file('names2.csv', 'rU') # names.csv
c1 = csv.reader(f1)

masterlist = list(c1)

for masterlist2 in masterlist:
 	List = sorted(masterlist2)

List2 = []
i = 1
value = 0

for names in List:
	List2.append([names, i])
	i += 1

for each in List2:
	name = each[0]
	pos = each[1]
	value += pos * findValue(name)

print value