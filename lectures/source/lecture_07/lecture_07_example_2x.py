lista = [5, 7, 8, 9, 3]

key = int(input("Δώσε στοιχείο που αναζητάς: "))

found = False
i = 0

while (i < 5) and (found is False):
    if lista[i] == key:
        thesi = i
        found = True
    else:
        i += 1

if found == True:
    print("Το %d βρίσκεται στη θέση %d." % (key, thesi))
else:
    print("Το %d δε βρίσκεται στη λίστα %d." % (key, thesi))
