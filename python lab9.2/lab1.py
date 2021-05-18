n = int(input())
b = int((n-1)/2)
j = int(n-1)
a = [['.'] * b + ['*'] + ['.'] * b for i in range(n)]
a[b] = ['*'] * n
for i in range(n):
	a[i][i] = '*'
	a[j][i] = '*'
	j -= 1
for row in a:
    print(' '.join([str(elem) for elem in row]))