lista = []
i = 0

while i < 100:
    lista.append(int(input("Δώσε αριθμό: ")))
    i += 1

i = 100

while i > 0:
    print(lista[i - 1])
    i -= 1
