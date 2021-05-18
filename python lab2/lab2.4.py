a = int(input('координат по x - ')) #x
b = int(input('координат по y - ')) #y
c = int(input('координат по x - ')) #x
d = int(input('координат по y - ')) #y
if a%2== b%2 and c%2 == d%2: #Если числа четные 
 print ('YES')
elif a%2 != b%2 and c%2 != d%2: #Если числа не четные
 print ('YES')
else:
 print('NO')