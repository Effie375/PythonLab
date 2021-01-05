list = [5, 7, 8, 9, 3]
found = False
thesi = i = 0

key = int(input("Δώσε στοιχείο που αναζητάς: ").strip())

while(i < len(list)) and (not found):
    if list[i] == key:
        thesi = i
        found = True
    else:
        i += 1

print(f"Το {key} βρίσκεται στη θέση {thesi}.")
