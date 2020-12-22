# Διάβασμα μεικτών απολαβών
miktes = input("Μικτές αποδοχές: ")

# Μετατροπή από str σε int
miktes = float(miktes)

# Υπολογισμός επί μέρους εισφορών
asfaleia = miktes * 0.03
foros = miktes * 0.05
loipa = miktes * 0.09

# Οι καθαρές απολαβές ειναι οι μεικτές μείον όλες τις εισφορές
kathara = miktes - asfaleia - foros - loipa

# Εκτύπωση
print("Μικτές αποδοχές:", miktes)
print("Ασφάλεια:", asfaleia)
print("Φόρος:", foros)
print("Λοιπές κρατήσεις:", loipa)
print("Καθαρές αποδοχές:", kathara)
