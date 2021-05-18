import re
f1 = open('f1.txt' , 'r')
f2 = open('f2.txt' , 'w')
q = f1.readlines()
for i in range(len(q)):
    q[i] = re.findall(r'[+-]?\d+',q[i])
    for g in range(len(q[i])):
        q[i][g] = int(q[i][g])
    print(sum(q[i]))
    f2.write(str(sum(q[i])))
f1.close()
f2.close()
