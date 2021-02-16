# Αρχικοποίηση μεταβλητής
MAX_PROSPATHEIES = 6

# Ζητάμε από το χρήστη να δώσει ρεκόρ αγώνων και το μετατρέπουμε σε πραγματικό
record = float(input("Δώσε ρεκόρ αγώνων: "))

# Όσο το ρεκόρ είναι μικρότερο το μηδενός ή είναι μεγαλύτερο του 10
while record < 0 or record > 10:
    # Ζητάμε από το χρήστη να δώσει το σωστό ρεκόρ αγώνων
    record = float(input("Δώσε το σωστό ρεκόρ αγώνων: "))

# Δημιουργία κενής λίστας
jumps = []

# Για MAX_PROSPATHEIES
for i in range(MAX_PROSPATHEIES):
    # Ζητάμε από το χρήστη να δώσει την προσπάθειά του και τη μετατρέπουμε σε πραγματικό
    prospatheia = float(input("Δώσε προσπάθεια αθλητή: "))
    # Αποθηκεύουμε την προσπάθεια στη λίστα
    jumps.append(prospatheia)

# Θεωρούμε ότι το αρχικό elaxisto και megisto είναι το πρώτο στοιχείο της λίστας
elaxisto = jumps[0]
megisto = jumps[0]

# Για κάθε προσπάθεια
for i in jumps:
    # Εάν η προσπάθεια είναι μικρότερη από το ελάχιστο
    if i < elaxisto:
        elaxisto = i
    # Εάν η προσπάθεια είναι μεγαλύτερη από το μέγιστο
    if i > megisto:
        megisto = i

# Εκτύπωση χειρότερης προσπάθειας
print("H χειρότερη προσπάθεια είναι: %.1f" % elaxisto)

# Εάν το μέγιστο είναι μεγαλύτερο από το ρεκόρ αγώνων
if megisto > record:
    print("Το νέο ρεκόρ είναι %.1f" % megisto)
# Αλλιώς εάν η διαφορά του ρεκόρ αγώνων από το μεγίστο απέχει λιγότερο από 0.5 μέτρα
elif record - megisto < 0.5:
    print("H καλύτερη προσπάθεια είναι: %.1f" % megisto)
# Αλλιώς οι προσπάθειες του αθλητή δεν ήταν ικανοποιητικές
else:
    print("Oι προσπάθειες του αθλητή δεν ήταν ικανοποιητικές.")