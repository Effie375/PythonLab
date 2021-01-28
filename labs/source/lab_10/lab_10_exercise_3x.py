# Δημιουργία συνάρτησης readMarks
def readMarks(N):
    # Δημιουργία κενής λίστας
    marks = []
    for i in range(N):
        # Ζητάμε από το χρήστη να δώσει βαθμό και το μετατρέπουμε σε ακέραιο
        mark = int(input("Δώσε βαθμό: "))
        # Αποθηκεύουμε το mark στη λίστα marks
        marks.append(mark)
    # Επιστρέφει το marks
    return marks


# Δημιουργία συνάρτησης getMax
def getMax(listaP):
    # Αρχικοποίηση μεταβλητής
    megisto = 0
    for i in listaP:
        # Εάν το στιγμιαίο στοιχείο της λίστας είναι μεγαλύτερο από το megisto
        if i > megisto:
            # Αποθηκεύουμε στο megisto το στιγμιαίο στοιχείο
            megisto = i
    # Επιστρέφει το megisto
    return megisto


# Δημιουργία συνάρτησης getMO
def getMO(listaP):
    # Αρχικοποίηση μεταβλητής
    souma = 0
    # Για κάθε στοιχείο της λίστας
    for i in listaP:
        souma += i
    # Επιστρέφει στη main το souma / len(listaP)
    return souma / len(listaP)


# Ζητάμε από το χρήστη να δώσει τα μαθήματα που δώθηκαν και το μετατρέπουμε σε ακέραιο
plithos = int(input("Πόσοι δώσανε το μάθημα:"))

# Καλούμε τη συνάρτηση readMarks
vathmoi = readMarks(plithos)

# Εκτύπωση του μέγιστου
print("Μέγιστος: %d" % getMax(vathmoi))
# Εκτύπωση του μέσου όρου
print("Mέσος όρος: %d" % getMO(vathmoi))
