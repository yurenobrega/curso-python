import functools
#letters = ["H", "E", "L", "L", "O"]

factorial = [5, 4, 3, 2, 1]
result = functools.reduce(lambda x, y,:x+y, factorial)
print(result)
