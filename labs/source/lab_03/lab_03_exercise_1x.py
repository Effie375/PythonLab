# Διάβασμα από το φοιτητή το όνομά του
onoma = input("Δώσε όνομα φοιτητή: ").strip()

# Διαβάζουμε από το φοιτητή το βαθμό του
proodos = float(input("Δώσε βαθμό προόδου: ").strip())

# Διαβάζουμε από το φοιτητή το βαθμό γραπτού του
graptο = float(input("Δώσε βαθμό γραπτών: ").strip())

# Υπολογίζουμε τον τελικό βαθμό
telikosVathmos = round(0.2 * proodos + 0.8 * graptο, 1)

# Εάν το όνομα τελειώνει σε 'ς' ή 's'
if (onoma[-1] == 's') or (onoma[-1] == 'ς'):
    # Σβήσε το τελευταίο γράμμα
    onoma = onoma[:-1]

# Κάνε το πρώτο γράμμα κεφαλαίο
onoma = onoma[0].upper() + onoma[1:]

# Ελέγχουμε εάν ο τελικός βαθμός είναι πάνω από 5
if telikosVathmos >= 5:
    print(f"{onoma} πέρασες!")
else:
    print(f"{onoma} απέτυχες!")
