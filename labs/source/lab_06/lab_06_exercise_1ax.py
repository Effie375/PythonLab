# Αρχικοποίηση μεταβλητών
MAX_ELEMENTS = 7
lista = []

# Για κάθε MAX_ELEMENTS
for i in range(MAX_ELEMENTS):
    # Διαβάζουμε από το χρήστη το βαθμό του και το μετατρεπουμε σε ακέραιο
    vathmos = int(input("Δώσε βαθμό: ").strip())
    # Αποθηκεύουμε το βαθμό στη λίστα
    lista.append(vathmos)

# Αρχικοποίηση μεταβλητών
athroisma = 0
k = 1

# Για κάθε στοιχείο της λίστας
for agwnisma in lista:
    # Κάθε φορά πενταπλασιάζουμε το κάθε αγώνισμα
    agwnisma *= 5 * k
    # Αυξάνουμε τη μεταβλητή k κατά 1
    k += 1
    # Αυξάνουμε το άθροισμα κατα agwnisma
    athroisma += agwnisma

# Υπολογισμός του μέσου όρου
mo = athroisma / MAX_ELEMENTS

# Εκτύπωση μέσου όρου
print(f"Ο μέσος όρος είναι {mo:.1f}.")
