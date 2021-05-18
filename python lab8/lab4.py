x = float(input())
y = float(input())
a = -1
b = 1
r = 2
def IsPointInArea(x,y):
    return (x-a)**2 + (y-b)**2 <= r**2 and y>=-x and y>=2*x+2
    return (x-a)**2+(y-b)**2 >=r**2 and y<=-x and y<=2*x+2
if IsPointInArea(x,y):
 print('Yes')
else:
 print ('No')
