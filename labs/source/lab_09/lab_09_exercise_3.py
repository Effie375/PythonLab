# Διάβασμα βαθμών
eksamino = []

for i in range(2):
    mathima = []
    for j in range(2):
        # Εισαγωγή δεδομένων
        vathmos = input("Βαθμός εξαμήνου %d και %d μάθημα: " % (i + 1, j + 1))
        vathmos = float(vathmos)
        mathima.append(vathmos)
        eksamino.append(mathima)

# Εμφάνιση βαθμών ανά εξάμηνο
print("Οι βαθμοί του φοιτητή είναι:", eksamino)

# Υπολογισμός μέγιστου με βάση το κάθε μάθημα
megVathmos = mathima[0]

for mathima in eksamino:
    for i in mathima:
        if megVathmos < i:
            megVathmos = i

# Εκτύπωση αποτελέσματος
print("O μέγιστος βαθμός είναι:", megVathmos)
