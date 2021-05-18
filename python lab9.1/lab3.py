n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
b = a[0][0] # max
for i in range(n):
    for j in range(m):
        if a[i][j] > b:
            b = a[i][j]
            q = i, j
print(' '.join([str(elem) for elem in q]))