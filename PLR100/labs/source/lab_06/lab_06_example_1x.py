# Αρχικοποίηση μεταβλητής
athroisma = 0

# Ζητάμε από το χρήστη να δώσει έναν αριθμό
number = int(input("Δώσε αριθμό: ").strip())

# Για number φορές
for i in range(number + 1):
    # Προσθέτουμε τον αριθμό στη μεταβλητή athroisma
    # και το εκχωρούμε στην ίδια μεταβλητή athroisma
    athroisma = athroisma + i

# Εκτύπωση αθροίσματος
print(f"Άθροισμα: {athroisma}")
