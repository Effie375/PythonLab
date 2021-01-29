# Αρχικοποίηση μεταβλητών
MAX_ELEMENTS = 20
names = []
marks = []

# Για MAX_ELEMENTS
for i in range(MAX_ELEMENTS):
    # Ζητάμε από το χρήστη να δώσει το όνομά του
    onoma = input("Δώσε όνομα: ")
    # Ζητάμε από το χρήστη να δώσει το βαθμό του και το μετατρέπουμε σε ακέραιο
    vathmos = int(input("Δώσε βαθμό: "))
    # Αποθηκεύουμε το όνομα στη λίστα names
    names.append(onoma)
    # Αποθηκεύουμε το βαθμό στη λίστα marks
    marks.append(vathmos)

# Αρχικοποίηση μεταβλητής
maxThesi = 0

# Για όσο είναι το μήκος της λίστας
for i in range(len(names)):
    if marks[i] > marks[maxThesi]:
        # Εκχωρούμε στη maxThesi το i
        maxThesi = i
# Εκτύπωση το όνομα του νικητή
print(names[maxThesi])
