# Διάβασμα βαθμών
eksamino = []

for i in range(2):
    mathima = []
    for j in range(2):
        vathmos = float(input("Δώσε βαθμό για %d εξάμηνο και %d μάθημα: "% (i+1, j+1)))
        mathima.append(vathmos)
        eksamino.append(mathima)

# Εμφάνιση βαθμών ανά εξάμηνο
print("Οι βαθμοί του φοιτητή είναι:", eksamino)

# Υπολογισμός μέγιστου με βάση το κάθε μάθημα
meg_vathmos=mathima[0]

for mathima in eksamino:
    for i in mathima:
        if meg_vathmos < i:
            meg_vathmos = i

print("O μέγιστος βαθμός είναι:", meg_vathmos)
