n=5
if n<=100 and n>=1:
    m=3
    if m<=10000 and n>=1: 
        a= [[int(j) for j in input().split()] for i in range(m)]
        a=[[2, 5], [5,1], [3, 1], [3, 2]]
        b=[]
        c=0
        for i in range(m):
            print(a[i])
