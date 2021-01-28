lista = [5, 7, 8, 9, 3]

found = False
i = 0

key = int(input("Δώσε στοιχείο που αναζητάς: "))

while (i < len(lista)) and (not found):
    if lista[i] == key:
        thesi = i
        found = True
    else:
        i += 1

print("Το %d βρίσκεται στη θέση %d." % (key, thesi))
