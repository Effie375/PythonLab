# Ζητάμε από το φοιτητή να δώσει το όνομα του
onoma = input("Δώσε όνομα φοιτητή: ").strip()

# Ζητάμε από το φοιτητή να δώσει το βαθμό προόδου
proodos = input("Δώσε βαθμό προόδου: ").strip()

# Ζητάμε από το φοιτητή να δώσει το βαθμό γραπτού
grapto = input("Δώσε βαθμό γραπτού: ").strip()

# Μετρατρέπουμε την πρόοδο από αλφαριθμητική τιμή σε float
proodos = float(proodos)

# Μετρατρέπουμε το γραπτό από αλφαριθμητική τιμή σε float
grapto = float(grapto)

# Υπολογίζουμε τον τελικό βαθμό του φοιτητή
telikosVathmos = proodos * 0.2 + grapto * 0.8

# Εμφανίζουμε το όνομα του φοιτητή και τον τελικό βαθμό του
print(f"\nΌνομα: {onoma}, Βαθμός: {telikosVathmos:.1f}")