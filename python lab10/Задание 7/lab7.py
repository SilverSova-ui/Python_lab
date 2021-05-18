import re
f1 = open('f1.txt' , 'r')
q = f1.read()
q = re.findall(r'@',q)
if len(q)> 0:
    print('Yes')
else:
    print('No')
f1.close()
