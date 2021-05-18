import re
f1 = open('f1.txt' , 'r')
f2 = open('f2.txt' , 'w')
sum1 = 0
q = f1.read()
q = re.findall(r'[+-]?\d+',q) # находим все числа без/c префиксами + и -
q =[int(i)for i in q] # приводим числа к int 
for i in q:
    sum1 +=i
f2.write(str(sum))
print(sum1)
f1.close()
f2.close()
