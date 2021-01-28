# Δημιουργία λίστας
lista = [1, 6, 3, 5, 4, 6]

# Ζητάμε από το χρήστη να δώσει στοιχείο που αναζητά στη λίστα και το μετατρεπουμε σε ακέραιο
key = int(input("Δώσε στοιχείο που αναζητάς: ").strip())

# Αρχικοποίηση μεταβλητών
done = True
thesi = 0

# Για κάθε στοιχείο της λίστας
for arithmos in lista:
    # Εάν το στιγμιαίο στοιχείο της λίστας είναι ίσο με το key
    if arithmos == key:
        # Εκτύπωση της θέσης όπου βρίσκεται το key
        print(f"To {key} βρίσκεται στην θέση {thesi} της λίστας.")
        # Το done γίνεται False
        done = False
    # Αυξάνουμε τη μεταβλητή thesi κατά 1
    thesi += 1

# Εάν το done παραμείνει True
if done == True:
    print("Το στοιχείο που αναζητάς δεν είναι στη λίστα.")
