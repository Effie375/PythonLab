a = int(input("a: "))
x = int(input("x: "))
y = float(input("y: "))

if a == 10:
    x = x % 2
    y = y**2
elif a == 3:
    x = x * 2
    y -= 1
elif a == 5:
    x = x + 4
    y += 7
else:
    x -= 3
    y += 1

print("x: %d , y: %.1f" % (x, y))