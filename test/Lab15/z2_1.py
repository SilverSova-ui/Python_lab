n = int(input())
m= int(input())
a = [[int(j) for j in input().split()] for i in range(m)]
v=[]
for i in range(n):
    for j in range(n):
        v.append(a.count(a[i][j]))
print(v)
