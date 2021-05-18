import re
n=int(input())
if n>=1 and n<=100:
    m=int(input())
    if m>=1 and m<=10000:
        a= [[int(j) for j in input().split()] for i in range(m)]
        b=[]
        v={}
        for i in range(m):
           if a[i] not in b:
                b.append(a[i])
        b=re.findall('\d+', str(b))
        for i in b:
            if b.count(i)!=n-1:
                v[i]=b.count(i)
        if len(v)!=0:
            print("No")
        else:
            print("Yes")
    else:
        print("Ошибка")
else:
    print("Ошибка")
