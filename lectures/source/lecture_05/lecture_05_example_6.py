lista = [3, 4, 1, 9, 4, 2]
key = int(input("Δώσε στοιχείο που αναζητάς: "))
i = 0

while i < len(lista):
    if key == lista[i]:
        thesi = i
    i += 1

print("Το στοιχείο που αναζητάς βρίσκεται στη θέση:", thesi)
