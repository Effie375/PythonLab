list = [3, 4, 1, 9, 7, 2, 1, 4, 5, 1]
key = int(input(("Δώσε στοιχείο που αναζητάς: "))
counter = 0

for k in list:
    if k == key:
        counter += 1

print("Το στοιχείο που αναζητάς εμφανίζεται", counter, "φορές στη λίστα.")