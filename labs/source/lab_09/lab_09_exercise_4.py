# Διάβασμα προσπαθειών
athlimata = []

for i in range(3):
    vathmoi = []
    for j in range(3):
        # Εισαγωγή δεδομένων
        vathmos = input("Βαθμός αθλήματος %d & προσπάθεια %d: " % (i+1, j+1))
        # Μετατροπή από str σε float
        vathmos = float(vathmos)
        vathmoi.append(vathmos)
    athlimata.append(vathmoi)

# Υπολογισμός και εμφάνιση αθλήματος με μεγαλύτερους βαθμούς
maxSum = 0

for vathmoi in athlimata:
    sum = 0
    for i in vathmoi:
        sum += i
        if sum > maxSum:
            maxSum = sum
            maxAthlima = vathmoi

# Εκτύπωση αποτελέσματος
print("Ο max βαθμός είναι:", maxAthlima, "και το άθροισμα είναι:", maxsum)

# Υπολογισμός μέγιστου βαθμού σε κάθε άθλημα
megVathmos = athlimata[0][0]

for vathmoi in athlimata:
    for i in vathmoi:
        if i > megVathmos:
            megVathmos = i

# Εκτύπωση αποτελέσματος
print("Ο μέγιστος βαθμός του αθλητή είναι:", megVathmos)

# Αναζήτηση φορών μέγιστου βαθμού σε κάθε άθλημα
vathmosCounter = 0

for vathmoi in athlimata:
    for i in vathmoi:
        if i == megVathmos:
            vathmosCounter += 1

# Εκτύπωση αποτελέσματος
print("O μέγιστος βαθμός βρέθηκε %d φορές." % (vathmosCounter))
