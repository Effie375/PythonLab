a = 3
x = 2
y = 4

if a == 10:
    x = x -2
    y = y ** 2
elif a == 3:
    x = x % 2
    y -= 1
elif a == 5:
    x = x * 4
    y -= 7
else:
    x -= 3
    y *= 1

print(x, y)
