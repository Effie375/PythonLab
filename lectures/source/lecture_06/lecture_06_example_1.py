# Αρχικοποίηση μεταβλητών
ΜAX_ELEMENTS = 5
lista = []

# Για ΜAX_ELEMENTS
for n in range(ΜAX_ELEMENTS):
    # Ζητάμε από το χρήστη να δώσει στοιχείο και το μετατρέπουμε σε ακέραιο
    num = int(input("Δώσε στοιχείο για την θέση %d: " % n))
    # Αποθηκεύουμε το στοιχείο στη λίστα
    lista.append(num)

# Εκτύπωση της λίστας
print(lista)
