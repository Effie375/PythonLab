# Διάβασμα από τον χρήστη
name = input("Δώσε όνομα φοιτητή: ").strip()

try:
    # Διάβασμα από τον χρήστη
    proodos = float(input("Δώσε βαθμό προόδου: ").strip())
    grapta = float(input("Δώσε βαθμό γραπτού: ").strip())
except ValueError:
    print("Μη έγκυρος βαθμός!")
else:
    # Υπολογισμός τελικού βαθμού
    telikos_vathmos = 0.2 * proodos + 0.8 * grapta
    # Εκτύπωση αποτελέσματος
    print(f"Όνομα φοιτητή: {name}.")
    print(f"Τελικός βαθμός: {telikos_vathmos:.1f}")
