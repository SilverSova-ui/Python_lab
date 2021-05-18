a = list(range(-10, 10))
b = sorted(a, key=lambda x: x if x >=0 else -x)
print(b)