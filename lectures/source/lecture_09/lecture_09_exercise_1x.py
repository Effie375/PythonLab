# Αρχικοποίηση μεταβλητών
MAX_MATHITES = 20
MAX_TRIMHNA = 3
lista = []

# Για MAX_MATHITES
for i in range(MAX_MATHITES):
    # Αποθηκεύουμε κενή υπολίστα στη λίστα
    lista.append([])
    # Αρχικοποίηση μεταβλητής
    sum = 0
    # Εκτύπωση Μαθητής
    print(f"\n-------- Μαθητής {i + 1} --------")
    # Για MAX_TRIMHNA
    for j in range(MAX_TRIMHNA):
        # Ζητάμε από το χρήστη να δώσει βαθμό τριμήνου
        vathmos = input(f"Δώσε βαθμό {j + 1}oυ τριμήνου: ").strip()
        # Έλεγχος ορθότητας
        while not vathmos.isdigit():
            # Ξανά ζητάμε από το χρήστη να δώσει βαθμό τριμήνου
            vathmos = input("Είπα δώσε βαθμό: ").strip()
        # Μετατρέπουμε την αλφαριθμητική τιμή σε ακέραια
        vathmos = int(vathmos)
        # Αυξάνουμε το sum κατά το vathmos
        sum += vathmos
        # Αποθηκεύουμε το βαθμό στη στιγμιαία υπολίστα
        lista[i].append(vathmos)
    # Αποθηκεύουμε το μέσο όρο του κάθε τριμήνου στη στιγμιαία υπολίστα της λίστας
    lista[i].append(sum // MAX_TRIMHNA)

print('\n', end='')

# Για MAX_MATHITES
for g in range(MAX_MATHITES):
    # Εκτύπωση του μέσου όρου από τον κάθε μαθητή
    print(f"O μέσος όρος του {g + 1}ου μαθητή είναι {list[g][MAX_TRIMHNA]}.")
