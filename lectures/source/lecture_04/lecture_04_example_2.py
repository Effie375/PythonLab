a = int(input("Δώσε 1ο αριθμό: ").strip())
x = int(input("Δώσε 2ο αριθμό: ").strip())
y = float(input("Δώσε 3ο αριθμό: ").strip())

if a == 10:
    x = x % 2
    y = y ** 2
elif a == 3:
    x = x * 2
    y -= 1
elif a == 5:
    x = x + 4
    y += 7
else:
    x -= 3
    y += 1

print(f"x: {x} , y: {y:.1f}")
