list = [9, 7, 8, 9, 3]

key = int(input("Δώσε στοιχείο που αναζητάς: ").strip())

thesi = 0

for i in list:
    if i == key:
        print(f"Το {key} βρίσκεται στη θέση {thesi}.")
    thesi += 1

k = 0

for i in list:
    if i == key:
        k += 1

print(f"Το {key} έχει εισαχθεί {k} φορές.")
