a = list(range(-10, 10))
b = list(map(lambda x: x if x%3 == 0 else 0, a))
print(b)