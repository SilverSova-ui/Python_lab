s = input()# ввод даных
c = (s[(len(s) + 1) // 2:]) # берет индекса cлева
n = (s[:(len(s) + 1) // 2]) # берет индекса справа
print (c + n )# перставить