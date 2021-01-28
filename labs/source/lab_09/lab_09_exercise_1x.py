# Αρχικοποίηση μεταβλητών
ΜAX_EXAMINA = 8
MAX_MATHIMATA = 6
eksamina = []

# Για ΜAX_EXAMINA
for i in range(ΜAX_EXAMINA):
    # Δημιουργία κενής λίστας
    vathmoi = []
    # Για MAX_MATHIMATA
    for j in range(MAX_MATHIMATA):
        # Ζητάμε από το χρήστη να δώσει ένα βαθμό και το μετατρεπουμε σε πραγματικό
        vathmos = float(input("Δώσε βαθμό για το %dο εξάμηνο: " % (i+1)))
        # Αποθηκεύουμε το βαθμό στη υπολίστα vathmoi
        vathmoi.append(vathmos)
    # Αποθηκεύουμε τις υπολίστες στη λίστα eksamina
    eksamina.append(vathmoi)

# Ζητάμε από το χρήστη να δώσει ένα εξάμηνο και το μετατρεπουμε σε ακέραιο
arEksaminou = int(input("Ποιο εξάμηνο θες να δείς; "))

# Αρχικοποίηση μεταβλητών
eksamino = eksamina[arEksaminou - 1]
souma = 0
perasmena = 0

# Για κάθε μάθημα του εξαμήνου
for mathima in eksamino:
    # Αυξάνουμε τη σούμα κατα μάθημα
    souma += mathima
    # Εάν ο βαθμός του μαθήματος είναι μεγαλύτερος ή ίσος με το 5
    if mathima >= 5:
        # Αυξάνουμε τη μεταβλητή perasmena κατά 1
        perasmena += 1

# Εκτύπωση του μέσου όρου
print("Ο μέσος όρος είναι: %.1f" % (souma / len(eksamino)))
# Εκτύπωση των περασμένων μαθημάτων
print("Πέρασες: %d μαθήματα." % perasmena)
