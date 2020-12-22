# Διάβασμα αποτελεσμάτων
onoma = input("Δώσε όνομα φοιτητή: ")
proodos = int(input("Βαθμός εργασίας: "))
grapto = int(input("Βαθμός γραπτού: "))

# Υπολογισμός τελικού βαθμού
telikosVathmos = proodos * 0.2 + grapto * 0.8

# Έλεγχος εαν είναι πάνω από 5
if telikosVathmos >= 5:
	print(onoma, "Πέρασες")
else:
	print(onoma, "Απέτυχες")
