f=open('f1.txt', 'r')
a=f.readlines()
b=[len(i) for i in a]
for i in a:
    if max(b)==len(i):
        print(i, end='')
f.close()
