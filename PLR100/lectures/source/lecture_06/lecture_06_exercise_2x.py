# Αρχικοποίηση μεταβλητών
ΜAX_ELEMENTS = 200
vath = []
sum = 0

# Για ΜAX_ELEMENTS
for i in range(ΜAX_ELEMENTS):
    # Ζητάμε απο το χρήστη να δώσει βαθμό και το μετατρέπουμε σε ακέραιο
    num = int(input("Δώσε βαθμό: ").strip())
    # Αποθηκεύουμε τον αριθμό στη λίστα vath
    vath.append(num)
    # Αυξάνουμε το sum κατά num
    sum += num

# Υπολογίζουμε το μέσο όρο
mo = sum / ΜAX_ELEMENTS

# Για ΜAX_ELEMENTS
for i in range(ΜAX_ELEMENTS):
    # Εάν το στιγμιαίο στοιχείο της λίστας είναι μεγαλύτερο από το μέσο όρο
    if vath[i] > mo:
        # Εκτύπωση το στιγμιαίο i
        print(i)
