a = [int(s) for s in input().split()]
b = set()
for i in a:
    if i in b:
        print('YES')
    else:
        print('NO')
        b.add(i)