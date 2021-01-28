# Δημιουργία λίστας
list = [3, 4, 1, 9, 7, 2, 1, 4, 5, 1]

# Ζητάμε από το χρήστη να δώσει στοιχείο που αναζητά και το μετατρέπουμε σε ακέραιο
key = int(input("Δώσε στοιχείο που αναζητάς: "))

# Αρχικοποίηση μεταβλητών
counter = 0
i = 0

# Για όσο το i είναι μικρότερο από το μήκος της λίστας
while i < len(list):
    # Εάν το στιγμιαίο στοιχείο της λίστας είναι ίσο με το key
    if list[i] == key:
        # Αυξάνουμε το counter κατά 1
        counter += 1
    # Αυξάνουμε το i κατά 1
    i += 1

# Εκτύπωση των φορών που εμφανίζεται το στοιχείο
print("Το στοιχείο που αναζητάς εμφανίζεται %d φορές στη λίστα." % counter)
