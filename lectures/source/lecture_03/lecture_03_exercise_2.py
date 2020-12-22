a = int(input("Δώσε έναν αριθμό: "))
b = int(input("Δώσε έναν άλλον αριθμό: "))
c = int(input("Δώσε έναν ακόμα αριθμό: "))

if (a + b) % 2 == 0:
    gin = a * (b // c)
    print(gin)
else:
    ypoloipo = c % (a + b)

print(ypoloipo)
