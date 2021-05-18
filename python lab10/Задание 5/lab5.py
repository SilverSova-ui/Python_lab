f=open('f1.txt', 'r')
a=f.read()
a=a[::-1]
print(''.join(a))
