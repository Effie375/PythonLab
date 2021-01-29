# Αρχικοποίηση μεταβλητών
MAX_ELEMENTS = 100
lista = []

# Για MAX_ELEMENTS
for i in range(MAX_ELEMENTS):
    # Ζητάμε από το χρήστη να δώσει αριθμό, το μετατρέπουμε σε ακέραιο και το αποθηκεύουμε στη λίστα
    lista.append(int(input("Δώσε αριθμό: ").strip()))

for i in range(MAX_ELEMENTS-1, -1, -1):
    # Εκτύπωση κάθε φορά το στιγμιαίο στοιχείο
    print(lista[i])
