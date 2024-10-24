def calcSum(n):
	total = 0
	while n > 0:
		total += n
		n -= 1
	return total

print(calcSum(10))
