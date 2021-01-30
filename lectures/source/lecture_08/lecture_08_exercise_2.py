# Δημιουργία συνάρτησης athroisma
def athroisma(plist):
    # Αρχικοποίηση μεταβλητής
    sum = 0
    # Για κάθε στοιχέιο της λίστας
    for item in plist:
        # Αυξάνουμε το sum κατά item
        sum += item
    # Επιστρέφει το sum
    return sum


# Αρχικοποίηση μεταβλητών
ΜΑΧ_PAIKTES = 10
ΜΑΧ_AGWNES = 15
pontoi = []
names = []

# Για ΜΑΧ_PAIKTES
for i in range(ΜΑΧ_PAIKTES):
    # Ζητάμε από το χρήστη να δώσει όνομα παίκτη
    name = input("\nΔώσε το όνομα του %dου παίκτη: " % (i + 1))
    # Αποθηκεύουμε το όνομα στη λίστα names
    names.append(name)
    # Για ΜΑΧ_AGWNES
    for j in range(ΜΑΧ_AGWNES):
        # Ζητάμε από το χρήστη να δώσει πόντους για τον αγώνα και το μετατρέπουμε σε ακέραιο
        pontos = int(input("Δώσε πόντους για τον %do αγώνα: " % (j + 1)))
        # Εάν το i είναι ίσο με το 0
        if (i == 0):
            # Αποθηκεύουμε κενή υπολίστα στη λίστα pontoi
            pontoi.append([])
        # Αποθηκεύουμε το πόντο στη στιγμιαία υπολίστα της λίστας pontoi
        pontoi[j].append(pontos)

# Τρέχει για κάθε αγώνα
for agwnas in range(ΜΑΧ_AGWNES):
    # Καλούμε τη συνάρτηση και παίρνουμε το άθροισμα των πόντων ανά αγώνα
    synoloPonton = athroisma(pontoi[agwnas])
    # Εκτύπωση αγώνας
    print("\n-------- Αγώνας %d --------" % (agwnas + 1))
    # Εκτύπωση σύνολο πόντων
    print("Σύνολο πόντων: %d" % synoloPonton)
    # Μηδενίζουμε τη θέση του καλύτερου παίκτη
    bestThesi = 0
    # Έστω ο καλύτερος παίκτης με τους περισσότερους πόντους είναι ο πρώτος
    best = pontoi[agwnas][bestThesi]
    # Τρέχει για κάθε παίκτη
    for paiktis in range(ΜΑΧ_PAIKTES):
        if pontoi[agwnas][paiktis] > best:
            # Εκχωρούμε στη bestThesi το paiktis
            bestThesi = paiktis

    # Εκτύπωση του καλύτερου παίκτη
    print("Καλύτερος παίκτης: %s" % names[bestThesi])
    # Εκτύπωση τους πόντους του καλύτερου παίκτη
    print("Πόντοι καλύτερου παίκτη: %d" % pontoi[agwnas][bestThesi])
