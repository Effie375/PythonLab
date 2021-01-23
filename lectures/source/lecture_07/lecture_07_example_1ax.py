lista = [9, 7, 8, 9, 3]

key = int(input("Δώσε στοιχείο που αναζητάς: "))

thesi = 0

for i in lista:
    if i == key:
        print("Το %d βρίσκεται στη θέση %d." % (key, thesi))
    thesi += 1
