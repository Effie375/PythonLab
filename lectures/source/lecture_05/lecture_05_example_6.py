# Δημιουργία λίστας
list = [3, 4, 1, 9, 4, 2]

# Ζητάμε από το χρήστη να δώσει στοιχείο που αναζητά και το μετατρέπουμε σε ακέραιο
key = int(input("Δώσε στοιχείο που αναζητάς: ").strip())

# Αρχικοποίηση μεταβλητής
i = 0

# Για όσο το i είναι μικρότερο από το μήκος της λίστας
while i < len(list):
    # Εάν το key είναι ίσο με το στιγμιαίο στοιχείο της λίστας
    if key == list[i]:
        # Εκχωρούμε στη thesi το στιγμιαίο i
        thesi = i
    # Αυξάνουμε το i κατά 1
    i += 1

# Εκτύπωση της θέσης από το στοιχείο που αναζητάει ο χρήστης
print(f"Το στοιχείο που αναζητάς βρίσκεται στη θέση: {thesi}")
