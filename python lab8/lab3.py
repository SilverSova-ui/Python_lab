def distance(x1,y1,x2,y2):
    return(((x1-x2)**2 + (y1-y2)**2)**0.5)
x1  =float(input('Введите координаты центра окружности'))
y2  =float(input('Введите координаты вне окружности'))
x2 =float(input())
y1 =float(input())
r  =float(input('Радиус окружности'))
def IsPointInCircle(x,y,xc,yc,r):
    return distance(x,y,xc,yc) <= r
if IsPointInCircle(x1,y1,x2,y2,r) == True:
    print('Yes')
else:
    print('No')















































