list = []

for i in range(100):
    list.append(int(input("Δώσε αριθμό: ").strip()))

for i in range(99, -1, -1):
    print(list[i])
