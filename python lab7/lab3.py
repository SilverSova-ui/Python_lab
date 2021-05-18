a=input().split()
for i in range(len(a)):
    if a[i-1]<a[i]:
        print(a[i], end=' ')
        

