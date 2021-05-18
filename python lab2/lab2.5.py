n = int(input())#натуральное число
if n % 4 == 0 and n % 100 != 0 or n %400  == 0: #условие
 print ('YES')
else:
 print ('NO')