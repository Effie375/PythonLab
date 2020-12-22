# Διάβασμα από τον χρήστη
onoma = input("Δώσε ονομα φοιτητή: ")
proodos = input("Βαθμός προόδου: ")
grapto = input("Βαθμός γραπτού: ")

# Μετατροπή από str σε int
proodos = int(proodos)
grapto = int(grapto)

# Υπολογισμός τελικού βαθμού
telikosVathmos = proodos * 0.2 + grapto * 0.8

# Εκτύπωση αποτελέσματος
print(onoma, telikosVathmos)
