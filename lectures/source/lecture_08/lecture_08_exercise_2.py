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
    name = input(f"\nΔώσε το όνομα του {i + 1}ου παίκτη: ").strip()
    names.append(name)
    for j in range(AGWNES):
        pontos = int(input(f"Δώσε πόντους για τον {j + 1}o αγώνα: ").strip())
        if (i == 0):
            pontoi.append([])
        pontoi[j].append(pontos)

# Τρέχει για κάθε αγώνα
for agwnas in range(AGWNES):
    # Καλούμε τη συνάρτηση και παίρνουμε το άθροισμα των πόντων ανα αγώνα
    synolo_ponton = athroisma(pontoi[agwnas])
    print(f"\n-------- Αγώνας {agwnas + 1} --------")
    print(f"Σύνολο πόντων: {synolo_ponton}")
    # Μηδενίζουμε τη θέση του καλύτερου παίκτη
    best_thesi = 0
    # Έστω ο καλύτερος παίκτης με τους περισσότερους πόντους είναι ο πρώτος
    best = pontoi[agwnas][best_thesi]
    # Τρέχει για κάθε παίκτη
    for paiktis in range(PAIKTES):
        if pontoi[agwnas][paiktis] > best:
            best_thesi = paiktis
    print(f"Καλύτερος παίκτης: {names[best_thesi]}")
    print(f"Πόντοι καλύτερου παίκτη: {pontoi[agwnas][best_thesi]}")
