lista = [8, 7, 8, 9, 3]

counter = 0

key = int(input("Δώσε στοιχείο που αναζητάς: "))

for k in lista:
    if k == key:
        counter += 1

print("Ο αριθμός %d έχει εισαχθεί %d φορές." % (key, counter))