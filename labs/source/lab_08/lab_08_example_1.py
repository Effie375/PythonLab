# Δημιουργία λίστας
lista = [1, 6, 3, 5, 4, 6]

# Εισαγωγή δεδομένων
key = int(input("Δώσε στοιχείο που αναζητάς: "))

# Αρχικοποίηση μεταβλητών
done = True
thesi = 0

for arithmos in lista:
    if arithmos == key:
        print(thesi)
        done = False
    thesi += 1

# Εκτύπωση αποτελέσματος
if done == True:
    print("Το στοιχείο που αναζητάς δεν είναι στη λίστα.")
