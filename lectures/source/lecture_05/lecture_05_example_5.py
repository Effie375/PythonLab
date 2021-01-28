# Αρχικοποίηση μεταβλητών
lista = [3, 4, 1, 9, 4, 2]
maxThesi = 0
i = 0

# Για όσο το i είναι μικρότερο από το μήκος της λίστας
while i < len(lista):
    if lista[i] > lista[maxThesi]:
        # Εκχωρούμε στο maxThesi το στιγμιαίο i
        maxThesi = i
    # Αυξάνουμε το i κατά 1
    i += 1

# Εκτύπωση της μέγιστης θέσης
print("Μέγιστη θέση:", maxThesi)
