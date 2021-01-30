# Aρχικοποίηση μεταβλητών
MAX_ELEMENTS = 5
lista = []

# Για MAX_ELEMENTS
for i in range(5):
    # Δημιουργία κενής λίστας
    ypolista = []
    # Για MAX_ELEMENTS - 1
    for j in range(MAX_ELEMENTS - 1):
        # Ζητάμε από το χρήστη να δώσει αριθμό και το μετατρέπουμε σε ακέραιο
        newNum = int(input("Δώσε αριθμό: "))
        # Αποθηκεύουμε τον αριθμό στην υπολίστα
        ypolista.append(newNum)
    # Αποθηκεύουμε την υπολίστα στη λίστα
    lista.append(ypolista)

# Εκτύπωση της λίστας
print(lista)