# Διάβασμα προσπαθειών
athlimata = []

for i in range(3):
    vathmoi = []
    for j in range(3):
        text = f"Βαθμός αθλήματος {i+1} και προσπάθεια {j+1}: "
        # Εισαγωγή δεδομένων
        vathmos = input(text).strip()
        # Μετατροπή από str σε float
        vathmos = float(vathmos)
        vathmoi.append(vathmos)
    athlimata.append(vathmoi)

# Υπολογισμός και εμφάνιση αθλήματος με μεγαλύτερους βαθμούς
maxsum = 0

for vathmoi in athlimata:
    sum = 0
    for i in vathmoi:
        sum += i
        if sum > maxsum:
            maxsum = sum
            maxathlima = vathmoi

# Εκτύπωση αποτελέσματος
print(f"Ο max βαθμός είναι: {maxathlima} και το άθροισμα είναι: {maxsum}")

# Υπολογισμός μέγιστου βαθμού σε κάθε άθλημα
meg_vathmos = athlimata[0][0]

for vathmoi in athlimata:
    for i in vathmoi:
        if i > meg_vathmos:
            meg_vathmos = i

# Εκτύπωση αποτελέσματος
print(f"Ο μέγιστος βαθμός του αθλητή είναι: {meg_vathmos}")

# Αναζήτηση φορών μέγιστου βαθμού σε κάθε άθλημα
vathmos_counter = 0

for vathmoi in athlimata:
    for i in vathmoi:
        if i == meg_vathmos:
            vathmos_counter += 1

# Εκτύπωση αποτελέσματος
print(f"O μέγιστος βαθμός βρέθηκε {vathmos_counter} φορές.")
