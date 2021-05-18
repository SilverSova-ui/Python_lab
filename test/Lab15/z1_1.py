n = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]
v=[]
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            v.append(a[i][j])
print(len(v)//2)
