a = list(range(-10, 10))
l = len(a)/2
b = sorted(a, key=lambda x: x if (x % 2 == 0) or (x % 3 ==0)else l)
print(b)