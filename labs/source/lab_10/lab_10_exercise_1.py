# Δημιουργία συνάρτησης readNames
def readNames(plithos):
    # Δημιουργία κενής λίστας
    onomata = []
    # Για όσο είναι το plithos
    for i in range(plithos):
        # Ζητάμε από το χρήστη να δώσει το όνομά του
        onoma = input("Δώσε όνομα:").strip()
        # Αποθηκεύουμε το όνομα στη λίστα onomata
        onomata.append(onoma)
    # Επιστρέφει τη λίστα onomata
    return onomata


# Δημιουργία συνάρτησης longestName
def longestName(list):
    # Αρχικοποίηση μεταβλητής
    maxLength = 0
    # Για κάθε όνομα στη λίστα
    for onoma in list:
        if len(onoma) > maxLength:
            maxLength = len(onoma)
    # Επιστρέφει το maxLength
    return maxLength


# Ζητάμε από το χρήστη να δώσει πλήθος και το μετατρέπουμε σε ακέραιο
plithos = int(input("Δώσε πλήθος: ").strip())
# Καλούμε τη συνάρτηση readNames
onomata = readNames(plithos)
# Καλούμε τη συνάρτηση longestName
x = longestName(onomata)

# Εκτύπωση του μήκους από το μακρύτερο όνομα
print(f"Το μακρύτερο όνομα έχει μήκος: {x}")
