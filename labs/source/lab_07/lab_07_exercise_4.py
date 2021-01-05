# Αρχικοποίηση μεταβλητών
grammata = "abcdefghijklmnopqrstuvwxyz"

# Εισαγωγή δεδομένων
leksi = input("Δώσε λέξη: ").lower()

for letter in grammata:
    counter = 0
    for grammaLeksis in leksi:
        if grammaLeksis == letter:
            counter += 1
    if counter != 0:
        # Εκτύπωση αποτελέσματος
        print("To γράμμα '%s' εμφανίστηκε %d φορές." % (letter, counter))
