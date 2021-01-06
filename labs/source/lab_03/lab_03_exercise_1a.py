# Διαβάζουμε από το φοιτητή το όνομα του
name = input("Δώσε το όνομά σου: ").strip()

try:
    # Διαβάζουμε από το φοιτητή το βαθμό του
    proodos = float(input("Δώσε βαθμό προόδου: ").strip())
    # Διαβάζουμε από το φοιτητή το βαθμό του γραπτού του
    grapta = float(input("Δώσε βαθμό γραπτών: ").strip())
except ValueError:
    print("Μη έγκυρος βαθμός!")
else:
    # Υπολογίζουμε τον τελικό βαθμό
    telikos_vathmos = round(0.2 * proodos + 0.8 * grapta, 1)
    # Ελέγχουμε εαν είναι πάνω από 5
    if telikos_vathmos >= 5:
        print("Πέρασες!")
    else:
        print("Απέτυχες!")
