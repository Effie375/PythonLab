lista = [5, 7, 8, 9, 3]

key = int(input("Δώσε στοιχείο που αναζητάς: ").strip())

for i in range(len(lista)):
    if lista[i] == key:
        thesi = i

print(f"Το {key} βρίσκεται στη {thesi} θέση.")
