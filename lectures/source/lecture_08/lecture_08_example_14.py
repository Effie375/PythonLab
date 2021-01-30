# Δημιουργία κενής λίστας
lista = []

# Για κάθε υπολίστα της λίστας
for ypolista in lista:
    # Αρχικοποίηση μεταβλητής
    sum = 0
    # Για κάθε στοιχείο της υπολίστας
    for i in ypolista:
        # Αυξάνουμε το sum κατά i
        sum += i

# Αποθηκεύουμε το sum στη λίστα
lista.append(sum)
