# Αρχικοποίηση μεταβλητών
MAX_ELEMENTS = 5
lista = []

# Για MAX_ELEMENTS
for i in range(MAX_ELEMENTS):
    # Ζητάμε από το χρήστη να δώσει ένα στοιχείο και το μετατρεπουμε σε ακέραιο
    num = int(input("Δώσε στοιχείο: ").strip())
    # Αποθηκεύουμε το στοιχείο στη λίστα
    lista.append(num)

# Εκτύπωση της μη ταξινομημένης λίστας
print(f"H μη ταξινομημένη λίστα είναι: {lista}")

for i in range(1, 5):
    for j in range(4, i - 1, -1):
        if lista[j - 1] > lista[j]:
            # Swap lista
            temp = lista[j - 1]
            lista[j - 1] = lista[j]
            lista[j] = temp

# Εκτύπωση της ταξινομημένης λίστας
print(f"H ταξινομημένη λίστα είναι: {lista}")
