# Δημιουργία λίστας
lista = [[2, 3, 4, 1],
         [7, 3, 3, 9],
         [6, 5, 5, 8],
         [1, 9, 4, 1],
         [0, 4, 7, 4]]

# Ζητάμε από το χρήστη να δώσει στοιχείο που αναζητά και το μετατρέπουμε σε ακέραιο
key = int(input("Δώσε στοιχείο που αναζητάς: "))

# Αρχικοποίηση μεταβλητών
found = False
i = 0
j = 0

# Για όσο το i είναι μικρότερο του 5 και ταυτόχρονα το found δεν ειναι False
while i < 5 and not found:
    # Για όσο το i είναι μικρότερο του 4 και ταυτόχρονα το found δεν ειναι False
    while j < 4 and not found:
        if key == lista[i][j]:
            # Εκτύπωση σε ποιο σημείο βρίσκεται το στοιχείο που αναζητά ο χρήστης
            print("Βρίσκεται στην %d υπολίστα στην %d θέση" % (i, j))
            # Το found γίνεται True
            found = True
        # Αυξάνουμε το j κατά 1
        j += 1
    # Μηδενίζουμε το j
    j = 0
    # Αυξάνουμε το i κατά 1
    i += 1