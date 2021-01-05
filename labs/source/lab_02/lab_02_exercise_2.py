# Διάβασμα μεικτών απολαβών
miktes = input("Μικτές αποδοχές: ")

# Μετατροπή από str σε float
miktes = float(miktes)

# Υπολογισμός επί μέρους εισφορών
asfaleia = miktes * 0.03
foros = miktes * 0.05
loipa = miktes * 0.09

# Οι καθαρές απολαβές ειναι οι μεικτές μείον όλες τις εισφορές
kathara = miktes - asfaleia - foros - loipa

# Εκτύπωση αποτελεσμάτων
print("Μικτές αποδοχές: %.2f" % miktes)
print("Ασφάλεια: %.2f" % asfaleia)
print("Φόρος: %.2f" % foros)
print("Λοιπές κρατήσεις: %.2f" % loipa)
print("Καθαρές αποδοχές: %.2f" % kathara)
