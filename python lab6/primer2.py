n = int(input())
l = 0
while n > 0:
	n //= 10 # это эквивалентно n = n // 10
	l += 1
print(l)