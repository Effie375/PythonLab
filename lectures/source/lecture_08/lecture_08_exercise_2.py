def athroisma(plist):
    sum = 0
    for item in plist:
        sum += item
    return sum


PAIKTES = 10
AGWNES = 15
pontoi = []
names = []

for i in range(PAIKTES):
    name = input("\nΔώσε το όνομα του %dου παίκτη: " % (i + 1))
    names.append(name)
    for j in range(AGWNES):
        pontos = int(input("Δώσε πόντους για τον %do αγώνα: " % (j + 1)))
        if (i == 0):
            pontoi.append([])
        pontoi[j].append(pontos)

# Τρέχει για κάθε αγώνα
for agwnas in range(AGWNES):
    # Καλούμε τη συνάρτηση και παίρνουμε το άθροισμα των πόντων ανα αγώνα
    synoloPonton = athroisma(pontoi[agwnas])
    print("\n-------- Αγώνας %d --------" % (agwnas + 1))
    print("Σύνολο πόντων: %d" % (synoloPonton))
    # Μηδενίζουμε τη θέση του καλύτερου παίκτη
    bestThesi = 0
    # Έστω ο καλύτερος παίκτης με τους περισσότερους πόντους είναι ο πρώτος
    best = pontoi[agwnas][bestThesi]
    # Τρέχει για κάθε παίκτη
    for paiktis in range(PAIKTES):
        if pontoi[agwnas][paiktis] > best:
            bestThesi = paiktis
    print("Καλύτερος παίκτης: %s" % (names[bestThesi]))
    print("Πόντοι καλύτερου παίκτη: %d" % (pontoi[agwnas][bestThesi]))
