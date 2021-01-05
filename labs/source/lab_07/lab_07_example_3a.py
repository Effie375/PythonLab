# Αρχικοποίηση μεταβλητών
counter = 0

# Εισαγωγή δεδομένων
leksi = input("Δώσε λέξη: ").strip()

for gramma in leksi:
    if gramma == 'e':
        counter += 1

# Εκτύπωση αποτελέσματος
print(counter)
