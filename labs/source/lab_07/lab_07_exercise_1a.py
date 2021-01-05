# Αρχικοποίηση μεταβλητών
sum = 0
ls = []
max_elements = 7

for i in range(max_elements):
    # Εισαγωγή δεδομένων
    vathmos = int(input("Δώσε βαθμό: ").strip())
    ls.append(vathmos)

# Αρχικοποίηση μεταβλητών
k = 1

for i in ls:
    i = i * 5 * k
    k = k + 1
    um = sum + i

# Υπολογισμός μέσου όρου
mo = sum / 7

# Εκτύπωση αποτελέσματος
print(f"Ο μέσος όρος είναι {mo}")
