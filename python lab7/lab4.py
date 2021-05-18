a = input().split()
for i in range(len(a)):
    if int(a[i+1]) * int(a[i]) > 0:
        print(a[i], a[i+1])
        break
