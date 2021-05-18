f=open('f1.txt', 'r+')
a=1
for i in f.readlines():
    for q in i.rstrip():
        q=chr(ord(q)+a)
        print(' '.join(b for b in q), end='')
    print()
    a+=1
f.close()
