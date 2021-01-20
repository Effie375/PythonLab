# Αρχικοποίηση μεταβλητών
i = 0
list = []

while i < 5:
    number = int(input("Δώσε αριθμό: "))
    list.append(number)
    i += 1

# Εισαγωγή δεδομένων
key = int(input("Δώσε στοιχείο που αναζητάς: "))

# Αρχικοποίηση μεταβλητών
found = False
j = 0

while (j < len(list) and not found):
    if list[j] == key:
        thesi = j
        found = True
    j += 1

# Εκτύπωση αποτελεσμάτων
if found == True:
    print("Το στοιχείο βρίσκεται στη θέση", thesi)
else:
    print("Το στοιχείο που αναζητάς δεν υπάρχει.")
