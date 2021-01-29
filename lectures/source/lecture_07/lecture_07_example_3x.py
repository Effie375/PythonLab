# Δημιουργία λίστας
lista = [5, 7, 8, 9, 3]

# Ζητάμε από το χρήστη να δώσει στοιχείο που αναζητά και το μετατρέπουμε σε ακέραιο
key = int(input("Δώσε στοιχείο που αναζητάς: ").strip())

# Αρχικοποίηση μεταβλητών
found = False
i = 0

# Για όσο το i είναι μικρότερο του 5 και ταυτόχρονα το found είναι ίσο με False
while (i < 5) and (found == False):
    # Εάν το στιγμιαίο στοιχείο της λίστας είναι ίσο με το key
    if lista[i] == key:
        # Εκχωρούμε στη thesi το i
        thesi = i
        # Το found γίνεται True
        found = True
    # Αυξάνουμε το i κατά 1
    i += 1

# Εάν το found είναι ίσο με True
if found == True:
    # Εκτύπωση τη θέση που βρίσκεται το key
    print(f"Το {key} βρίσκεται στη {thesi} θέση.")
# Αλλιώς σε οποιαδήποτε άλλη περίπτωση
else:
    # Εκτύπωση ότι το key δε βρίσκεται στη λίστα
    print(f"Το {key} δε βρίσκεται στη λίστα {lista}.")
