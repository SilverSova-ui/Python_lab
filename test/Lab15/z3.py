n = int(input())
if n>0 and n<=100:
    a = [[int(j) for j in input().split()] for i in range(n)]
    print()
    b = [int(j) for j in input().split()]
v=[]
for i in range(n):
    for j in range(n):
        if a[i][j]==1 and b[i]!=b[j]:
            v.append(1)
print(len(v)//2)                
            
                
