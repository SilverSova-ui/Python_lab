a=input().split()
for i in range(len(a)):
    if int(a[i])%2!=0:
        if int(a[i])<int(a[i+1]):
            b=a[i]
            print(b)
            break
else:
    print(0)
