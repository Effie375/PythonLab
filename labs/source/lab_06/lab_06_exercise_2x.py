# Αρχικοποίηση μεταβλητών
MAX_ELEMENTS = 10
lista = []

# Για κάθε MAX_ELEMENTS
for i in range(MAX_ELEMENTS):
    # Ζητάμε από το χρήστη να δώσει έναν αριθμό και τον αποθηκεύουμε στη λίστα
    lista.append(int(input("Δώσε αριθμό: ").strip()))

# Ζητάμε απο το χρήστη να δώσει αριθμό για έλεγχο διαιρετέων
num = int(input("Δώσε αριθμό για έλεγχο διαιρετέων: ").strip())

# Για κάθε αριθμό στη λίστα
for arithmos in lista:
    # Εάν ο αριθμός διαιρείται
    if arithmos % num == 0:
        # Εμφανίζουμε τον αριθμό
        print(arithmos)
