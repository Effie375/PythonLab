# Διάβασμα από τον χρήστη
name = input("Δώσε όνομα φοιτητή: ")
proodos = input("Δώσε βαθμό προόδου: ")
grapto = input("Δώσε βαθμό γραπτού: ")

# Μετατροπή από str σε int
proodos = int(proodos)
grapto = int(grapto)

# Υπολογισμός τελικού βαθμού
telikosVathmos = proodos * 0.2 + grapto * 0.8

# Εκτύπωση αποτελέσματος
print(name, telikosVathmos)