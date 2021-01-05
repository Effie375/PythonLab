# Διάβασμα προσπαθειών
athlimata = []

for i in range(3):
    vathmoi = []
    for j in range(3):
        vathmos = input("Βαθμός αθλήματος %d & προσπάθεια %d: " % (i+1, j+1))
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

print("Ο max βαθμός είναι:", maxathlima, "και το άθροισμα είναι:", maxsum)

# Υπολογισμός μέγιστου βαθμού σε κάθε άθλημα
meg_vathmos = athlimata[0][0]

for vathmoi in athlimata:
    for i in vathmoi:
        if i > meg_vathmos:
            meg_vathmos = i

print("Ο μέγιστος βαθμός του αθλητή είναι:", meg_vathmos)

# Αναζήτηση φορών μέγιστου βαθμού σε κάθε άθλημα
vathmos_counter = 0

for vathmoi in athlimata:
    for i in vathmoi:
        if i == meg_vathmos:
            vathmos_counter += 1

print("O μέγιστος βαθμός βρέθηκε %d φορές." % (vathmos_counter))
