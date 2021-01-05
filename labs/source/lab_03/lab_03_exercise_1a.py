# Διάβασμα από τον χρήστη
name = input("Δώσε το όνομά σου: ").strip()

try:
    # Διάβασμα αποτελεσμάτων
    proodos = float(input("Δώσε βαθμό προόδου: ").strip())
    grapta = float(input("Δώσε βαθμό γραπτών: ").strip())
except ValueError:
    print("Μη έγκυρος βαθμός!")
else:
    # Υπολογισμός τελικού βαθμού
    telikos_vathmos = round(0.2 * proodos + 0.8 * grapta, 1)
    # Έλεγχος εαν είναι πάνω από 5
    if telikos_vathmos >= 5:
        print("Πέρασες!")
    else:
        print("Απέτυχες!")
