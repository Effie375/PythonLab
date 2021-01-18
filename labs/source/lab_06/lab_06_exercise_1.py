# Αρχικοποίηση μεταβλητών
sum = 0
ls = []

for i in range(7):
    # Εισαγωγή δεδομένων
    vathmos = int(input("Δώσε βαθμό: "))
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
print("Ο μέσος όρος είναι", mo)
