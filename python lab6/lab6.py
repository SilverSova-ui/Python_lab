x = int(input()) #ввод даных
p = int(input()) #процент
y = int(input()) #рубли
i=1
while (x+x//p)<y
 x+=x//p
 i+=1
print(i)