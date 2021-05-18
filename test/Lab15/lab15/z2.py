n = int(input())
if n>0 and n<=100:
    m = int(input())
    if m>=0 and m<=n*(n-1)//2:
        a = [[int(j) for j in input().split()] for i in range(m)]
        v=[]
        b={}
        for i in range(m):
            for j in range(2):
                if a[i][j]>1 and a[i][j]<=n:
                    v.append(a[i][j])
        for i in range(len(v)):
            b[v[i]]=v.count(v[i])
        print(b.values())
    else:
        print("Ошибка")
else:
    print("Ошибка")
