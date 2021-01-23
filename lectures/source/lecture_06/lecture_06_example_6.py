lista = [5, 7, 8, 9, 3]

found = False
i = 0

key = int(input("Δώσε στοιχείο που αναζητάς: ").strip())

while (i < len(lista)) and (not found):
    if lista[i] == key:
        thesi = i
        found = True
    else:
        i += 1

print(f"Το {key} βρίσκεται στη {thesi} θέση.")
