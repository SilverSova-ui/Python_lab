import math
x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
def distance(x1, y1, x2, y2):
    b=(x1+x2)**2+(y1+y2)**2
    c=math.sqrt(b)
    print(round(c,5))
distance(x1, y1, x2, y2)



    
