# Διάβασμα από τον χρήστη
onoma = input("Ποιο είναι το όνομα σου: ")
hlikia = input("Ποια είναι η ηλικία σου: ")

# Μετατορπή της ηλικίας σε int από str
hlikia = int(hlikia)

twrinoEtos = 2020

# Υπολογισμός έτους γέννησης
etosGennhshs = twrinoEtos - hlikia

# Υπολογισμός χρονιάς που θα γίνει 100
ekatoXronwn = etosGennhshs + 100

print("O/H", onoma, "θα γίνει 100 το έτος", ekatoXronwn)