s = input() #ввод даных
z = s[:s.find(' ')] #1 слово
t = s[s.find(' ') + 1:]#2 слово
print(t + ' ' + z)