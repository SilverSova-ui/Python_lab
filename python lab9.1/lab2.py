n = int(input())
m = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(m):
        if i < j:
            a[i][j]= 0
        elif i > j:
            a[i][j] = 2
        else:
            a[i][j] = 5
for row in a:
    print(' '.join([str(elem) for elem in row]))
