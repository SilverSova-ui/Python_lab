import re
a = {}
f1 = open('f1.txt' , 'r')
q = f1.read().strip()
q = re.findall(r'\w+', q)
for i in q:
    if i in a:
        a[i]+=1
    else:
        a[i]=0
    print(a[i], end = ' ')
