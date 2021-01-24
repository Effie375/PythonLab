# Αρχικοποίηση μεταβλητών
MAX_ATHLIMATA = 4
MAX_PROSPATHEIES = 3
athlimata = []

# Για MAX_ATHLIMATA
for i in range(MAX_ATHLIMATA):
    # Δημιουργία κενής λίστας
    vathmoi = []
    # Για MAX_PROSPATHEIES
    for j in range(MAX_PROSPATHEIES):
        # Αποθηκεύουμε στη μεταβλητή text το κείμενο που θέλουμε να εμφανίσουμε στο χρήστη
        text = f"Βαθμός {i+1}ου αθλήματος και {j+1}η προσπάθεια: "
        # Ζητάμε από το χρήστη να μας δώσει βαθμό αθλήματος και την προσπάθειά του 
        vathmos = input(text).strip()
        # Το μετατρέπουμε σε πραγματική τιμή
        vathmos = float(vathmos)
        # Αποθηκεύουμε το βαθμό στην υπολίστα vathmos
        vathmoi.append(vathmos)
    # Αποθηκεύουμε την υπολίστα vathmoi στη λίστα athlimata
    athlimata.append(vathmoi)

# Έστω ότι το μεγαλύτερο άθροισμα βρίσκεται στην υπολίστα με τη θέση 0
maxSum = 0

# Για κάθε βαθμό των αθλημάτων
for vathmoi in athlimata:
    # Αρχικοποίηση μεταβλητής
    sum = 0
    # Για κάθε στοιχείο της υπολίστας vathmoi
    for i in vathmoi:
        # Αυξάνουμε τη μεταβλητή sum κατά 1
        sum += i
        # Εάν η τιμή της μεταβλητής sum είναι μεγαλύτερη από το maxSum που ορίσαμε
        if sum > maxSum:
            maxSum = sum
            maxathlima = vathmoi

# Εκτύπωση του μέγιστου βαθμού και το άθροισμά της υπολίστας
print(f"Ο max βαθμός είναι: {maxathlima} και το άθροισμα είναι: {maxSum}")

# Έστω ότι ο μέγιστος βαθμός βρίσκεται στην υπολίστα με τη θέση 0 και το στοιχείο της στη θέση 0
megVathmos = athlimata[0][0]

# Για κάθε βαθμό των αθλημάτων
for vathmoi in athlimata:
    # Για κάθε στοιχείο της υπολίστας vathmoi
    for i in vathmoi:
        # Εάν το στιγμιαίο στοιχείο της υπολίστας είναι μεγαλύτερο από το μέγιστο βαθμό που ορίσαμε
        if i > megVathmos:
            # Εκχωρούμε στη μεταβλητή megVathmos το στιγμιαίο στοιχείο της υπολίστας
            megVathmos = i

# Εκτύπωση του μέγιστου βαθμού του αθλητή
print(f"Ο μέγιστος βαθμός του αθλητή είναι: {megVathmos}")

# Αρχικοποίηση μεταβλητής
vathmosCounter = 0

# Για κάθε βαθμό των αθλημάτων
for vathmoi in athlimata:
    # Για κάθε στοιχείο της υπολίστας vathmoi
    for i in vathmoi:
        # Εάν το στιγμιαίο στοιχείο της υπολίστας είναι ίσο με το μέγιστο βαθμό 
        if i == megVathmos:
            # Αυξάνουμε τη μεταβλητή vathmosCounter κατά 1
            vathmosCounter += 1

# Εκτύπωση των φορών που εμφανίζεται ο μέγιστος βαθμός
print(f"O μέγιστος βαθμός βρέθηκε {vathmosCounter} φορές.")
