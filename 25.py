found = False
total = 0
n = 0
i = 3
saved = []
f1 = 1
f2 = 1

# def F(num):
# 	result = 0
# 	if num < 1:
# 		result = 0
# 	elif num == 1 or num == 2:
# 		result = 1
# 	else:
# 		result = F(num - 1) + F(num - 2)
# 	return result

def F(fib1, fib2):
	result = 0
	result = fib1 + fib2
	fib2 = fib1
	fib1 = result
	return (result, fib1, fib2)


while not found:
	total, f1, f2 = F(f1, f2)
	print "F(%d) = %d" % (i, total)
	if len(str(total)) > 999:
		print "Answer = %dth term, %d" % (i, total)
		break
	i += 1