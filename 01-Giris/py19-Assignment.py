x, y, z = 23, 20, 30
print(x, y, z)

x, y = y, x  # x ve y değerleri değişir
print(x, y, z)

x, y = y, x

x += 5
x -= 5
x *= 5
x /= 5
x //= 5  # tam bölme
x **= 5
print(x)
x %= 5


values = 1, 2, 3  # tupple
print(values)
print(type(values))

x, y, z = values
print(x, y, z)

values2 = 1, 2, 3, 4, 5, 6, 7
x, y, *z = values2 # *z fazla elemanları z ye atar
print(x, y, z)


