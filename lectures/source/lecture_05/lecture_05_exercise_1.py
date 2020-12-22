list = []
i = 0

while i < 100:
    list.append(int(input("Δώσε αριθμό: ")))
    i += 1

i = 100

while i > 0:
    print(list[i - 1])
    i -= 1
