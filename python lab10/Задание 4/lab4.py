f=open('f1.txt', 'r')
a=f.readlines()
a.reverse()
print(''.join(a).strip('\n'))
