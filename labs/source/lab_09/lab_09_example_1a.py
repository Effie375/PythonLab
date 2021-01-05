# Δημιουργία λίστας
list = [1, 6, 3, 5, 4, 6]

# Εισαγωγή δεδομένων
key = int(input("Δώσε στοιχείο που αναζητάς: ").strip())

# Αρχικοποίηση μεταβλητών
found = False
thesi = 0

for i in list:
    if i == key:
        print(f"Το {key} βρίσκεται στη {thesi} θέση της λίστας.")
        found = True
    thesi += 1

# Εκτύπωση αποτελέσματος
if found is False:
    print("Το στοιχείο που αναζητάς δεν είναι στη λίστα.")
