# Αρχικοποίηση μεταβλητών
counter = 0

# Εισαγωγή δεδομένων
leksi = input("Δώσε λέξη: ")

for gramma in leksi:
    if gramma == 'e':
        counter += 1

# Εκτύπωση αποτελέσματος
print(counter)
