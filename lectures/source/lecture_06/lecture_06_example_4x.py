# Αρχικοποίηση μεταβλητών
maxThesi = 0
thesi = 0

# Δημιουργία λίστας
lista = [5, 7, 8, 9, 3]

# Για κάθε στοιχείο της λίστας
for item in lista:
    if item > lista[maxThesi]:
        # Εκχωρούμε στη maxThesi τη thesi
        maxThesi = thesi
    # Αυξάνουμε τη thesi κατά 1
    thesi += 1

# Εκτύπωση της maxThesi με τον 1ο τρόπο
print(f"H maxThesi με τον 1ο τρόπο: {maxThesi}")

# Για όσο είναι το μήκος της λίστας
for i in range(len(lista)):
    if lista[i] > lista[maxThesi]:
        # Εκχωρούμε στη maxThesi τo i
        maxThesi = i

# Εκτύπωση της maxThesi με τον 2ο τρόπο
print(f"H maxThesi με τον 2ο τρόπο: {maxThesi}")
