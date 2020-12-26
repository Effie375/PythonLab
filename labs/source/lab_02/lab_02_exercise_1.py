# Διάβασμα από τον χρήστη
onoma = input("Δώσε ονομα φοιτητή: ")
proodos = input("Δώσε βαθμό προόδου: ")
grapta = input("Δώσε βαθμό γραπτών: ")

# Μετατροπή από str σε int
proodos = int(proodos)
grapta = int(grapta)

# Υπολογισμός τελικού βαθμού
telikosVathmos = proodos * 0.2 + grapta * 0.8

# Εκτύπωση αποτελέσματος
print(onoma, telikosVathmos)