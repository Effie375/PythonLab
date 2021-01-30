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
    print("\n-------- Μαθητής %d --------" % (i + 1))
    # Για MAX_TRIMHNA
    for j in range(MAX_TRIMHNA):
        # Ζητάμε από το χρήστη να δώσει βαθμό τριμήνου
        vathmos = input("Δώσε βαθμό %doυ τριμήνου: " % (j + 1))
        # Έλεγχος ορθότητας
        while not vathmos.isdigit():
            # Ξανά ζητάμε από το χρήστη να δώσει βαθμό τριμήνου
            vathmos = input("Είπα δώσε βαθμό: ")
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
    print("O μέσος όρος του %dου μαθητή είναι %d." % ((g + 1), (lista[g][MAX_TRIMHNA])))
