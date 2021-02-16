# Ζητάμε από το χρήστη να δώσει το όνομά του
onoma = input("Πώς σε λένε; ")

# Ζητάμε από το χρήστη να δώσει την ηλικία του
ilikia = input("Ποια είναι η ηλικία σου: ")

# Μετατροπή από str σε int
ilikia = int(ilikia)

# Τωρινό έτος
twrinoEtos = 2021

# Υπολογισμός έτους γέννησης
etosGennhshs = twrinoEtos - ilikia

# Υπολογισμός χρονιάς που θα γίνει 100
ekatoXronwn = etosGennhshs + 100

# Εκτύπωση αποτελέσματος
print("%s θα γίνεις 100 το έτος %d." % (onoma, ekatoXronwn))
