# Αρχικοποίηση μεταβλητών
ΜAX_MATHIMATA = 2
ΜΑΧ_ΕΧΑΜΗΝΑ = 2
eksamino = []

# Για ΜΑΧ_ΕΧΑΜΗΝΑ
for i in range(ΜΑΧ_ΕΧΑΜΗΝΑ):
    # Δημιουργία κενής λίστας
    mathima = []
    # Για ΜAX_MATHIMATA
    for j in range(ΜAX_MATHIMATA):
        # Ζητάμε από το χρήστη να μας δώσει βαθμό για το μάθημα του εξαμήνου
        vathmos = input(f"Βαθμός {i + 1}ου εξαμήνου και {j + 1}ο μάθημα: ").strip()
        # Το μετατρέπουμε σε πραγματική τιμή
        vathmos = float(vathmos)
        # Αποθηκεύουμε το βαθμό στην υπολίστα mathima
        mathima.append(vathmos)
    # Αποθηκεύουμε την υπολίστα mathima στη λίστα eksamino
    eksamino.append(mathima)

# Εκτύπωση των βαθμών του φοιτητή
print(f"Οι βαθμοί του φοιτητή είναι: {eksamino}")

# Έστω ότι ο μέγιστος βαθμός είναι ο βαθμός που βρίσκεται στη θέση 0
megVathmos = mathima[0]

# Για κάθε μάθημα του εξαμήνου
for mathima in eksamino:
    # Για κάθε στοιχείο στην υπολίστα
    for i in mathima:
        # Εάν ο μέγιστος βαθμός είναι μικρότερος από το στιγμιαίο στοιχείο της υπολίστας
        if megVathmos < i:
            # Εκχωρούμε στη μεταβλητή megVathmos το στιγμιαίο στοιχείο της υπολίστας
            megVathmos = i

# Εκτύπωση του μέγιστου βαθμού
print(f"O μέγιστος βαθμός είναι: {megVathmos}")
