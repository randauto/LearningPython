# cau lenh continue.
for x in 1, 2, 3, 4, 5:
    if (x % 2 == 0):
        continue
    print("x = ", x, " la so le")
# cau lenh break.
for x in 1, 2, 3, 4, 5, 6, 7, 8:
    if x == 4:
        break
    print("x = ", x)

for x in range(3):
    for y in range(6):
        if y == 3:
            break
        print("x, y = ", x, y, sep=' ')
