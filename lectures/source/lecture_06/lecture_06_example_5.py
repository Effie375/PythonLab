lista = [5, 7, 8, 9, 3]

key = int(input("Δώσε στοιχείο που αναζητάς: "))

for i in range(len(lista)):
    if lista[i] == key:
        thesi = i

print("Το %d βρίσκεται στη θέση %d." % (key, thesi))
