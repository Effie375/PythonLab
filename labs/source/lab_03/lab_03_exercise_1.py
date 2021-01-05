# Διάβασμα αποτελεσμάτων
onoma = input("Δώσε όνομα φοιτητή: ")
proodos = int(input("Δώσε βαθμό προόδου: "))
grapta = int(input("Δώσε βαθμό γραπτών: "))

# Υπολογισμός τελικού βαθμού
telikosVathmos = proodos * 0.2 + grapta * 0.8

# Έλεγχος εαν είναι πάνω από 5
if telikosVathmos >= 5:
    print(onoma, "Πέρασες")
else:
    print(onoma, "Απέτυχες")
