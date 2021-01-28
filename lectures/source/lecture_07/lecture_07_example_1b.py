lista = [9, 7, 8, 9, 3]

key = int(input("Δώσε στοιχείο που αναζητάς: "))

k = 0

for i in lista:
    if i == key:
        k += 1

print("Το %d έχει εισαχθεί %d φορές." % (key, k))
