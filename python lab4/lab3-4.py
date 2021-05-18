n = int(input('Введите общее кол-во карточек -'))
sum1 = 0
sum2 = 0
for i in range(n+1):
	sum1 +=i
for i in range(n):
	sum2 +=i+int(input('Введите нормера оставшихся карточек -'))
print(sum1-sum2)