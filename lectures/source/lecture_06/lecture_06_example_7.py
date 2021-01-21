lista = [3, 4, 1, 9, 4, 2]

key = int(input("Δώσε στοιχείο που αναζητάς: "))

for i in range(len(lista)):
    if lista[i] == key:
        thesi = i

print("Το στοιχείο που αναζητάς βρίσκεται στη θέση:", thesi)
