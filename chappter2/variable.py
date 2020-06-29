# gan gia tri cho bien
x = "Toi tu hoc lap trinh Python"
print(x)
print("Dia chi o nho: ", id(x))

x = 123
y = 123

print("Dia chi o nho x tro toi: ", id(x))
print("Dia chi o nho y tro toi: ", id(y))
x = 321
print("Dia chi o nho x tro toi: ", id(x))
print("Dia chi o nho y tro toi: ", id(y))

# bai tap 3
a, b, c = 1, 2, 3
a, b, c = b, c, a
print(a, b, c)
