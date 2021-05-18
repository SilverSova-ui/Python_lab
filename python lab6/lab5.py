x=int(input()) #ввод даных
y=int(input())
i=0
while (x+x//10)<y:
    x+=x//10
    i+=1
print(i)
