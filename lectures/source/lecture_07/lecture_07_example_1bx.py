lista = [9, 7, 8, 9, 3]

key = int(input("Δώσε στοιχείο που αναζητάς: ").strip())

k = 0

for i in lista:
    if i == key:
        k += 1

print(f"Το {key} έχει εισαχθεί {k} φορές.")
