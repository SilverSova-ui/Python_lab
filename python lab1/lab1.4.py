n = int(input()) #ввод переменой
h = n %(24*60) # часы
a = n //60 
m = n % 60 # минуты
print(a, n, sep = ':') #резултат