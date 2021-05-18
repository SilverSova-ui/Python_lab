from random import*
n = int(input())
a = [[randrange(0,1)]  for i in range(n)]
for row in a:
    print(' '.join([str(elem) for elem in row]))
