# Αρχικοποίηση μεταβλητών
MAX_ELEMENTS = 10
MAX_LISTES = 5
lista = []

# MAX_LISTES
for i in range(MAX_LISTES):
    # Δημιουργία κενής λίστας
    ypolista = []
    # Για MAX_ELEMENTS
    for j in range(MAX_ELEMENTS):
        # Ζητάμε από το χρήστη να δώσει έναν αριθμό και το μετατρεπουμε σε ακέραιο
        n = int(input("Δώσε αριθμό: "))
        # Αποθηκεύουμε τον αριθμό στην υπολίστα
        ypolista.append(n)
    # Αποθηκεύουμε την υπολίστα στη λίστα
    lista.append(ypolista)

# Έστω ότι το μέγιστο άθροισμα το έχει η υπολίστα στη θέση 0
megAthroisma = 0

# Για κάθε υπολίστα της λίστας
for ypolista in lista:
    # Αρχικοποίηση του μετρητή
    athroisma = 0
    # Για κάθε στοιχείο της υπολίστας
    for i in ypolista:
        # Αυξάνουμε τη μεταβλητή athroisma κατά 1
        athroisma += i
    # Εάν το άθροισμα είναι μεγαλύτερο από αυτό που ορίσαμε
    if athroisma > megAthroisma:
        # Το αντικαθηστούμε με το πλεόν μεγαλύτερο
        megAthroisma = athroisma
        # Εκχωρούμε στη μεταβλητή megLista τη μεγαλύτερη υπολίστα
        megLista = ypolista

# Εκτύπωση της υπολίστας με το μεγαλύτερο άθροισμα
print("Η υπολίστα με το μεγαλύτερο άθροισμα είναι %s" % megLista)
