# Αρχικοποίηση μεταβλητών
MAX_ELEMENTS = 5
lista = []
i = 0

# Για όσο το i είναι μικρότερο από το MAX_ELEMENTS
while i < MAX_ELEMENTS:
    # Ζητάμε από το χρήστη να δώσει στοιχείο και το μετατρέπουμε σε ακέραιο
    num = int(input(f"Δώσε στοιχείο για την {i} θέση: ").strip())
    # Προσθέτουμε το στοιχείο στη lista
    lista.append(num)
    # Αυξάνουμε το i κατά 1
    i += 1

# Εκτύπωση της λίστας
print(f"Η λίστα μας είναι: {lista}")
