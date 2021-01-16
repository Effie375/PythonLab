list = [5, 7, 8, 9, 3]

key = int(input("Δώσε στοιχείο που αναζητάς: ").strip())

found = False
i = 0

while (i < 5) and (found is False):
    if list[i] == key:
        thesi = i
        found = True
    i += 1

if found is True:
    print(f"Το {key} βρίσκεται στη {thesi} θέση.")
else:
    print(f"Το {key} δε βρίσκεται στη λίστα {list}.")
