# Δημιουργία λίστας
list = [1, 6, 3, 5, 4, 6]

key = int(input("Δώσε στοιχείο που αναζητάς: ").strip())

found = False
thesi = 0

for i in list:
    if i == key:
        print(f"Το {key} βρίσκεται στη {thesi} θέση της λίστας.")
        found = True
    thesi += 1

if found is False:
    print("Το στοιχείο που αναζητάς δεν είναι στη λίστα.")
