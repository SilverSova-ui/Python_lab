n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i < j:
            a[i][j]= abs(i-j)
        elif i > j:
            a[i][j] = abs(i-j)
for row in a:
    print(' '.join([str(elem) for elem in row]))