# Ζητάμε από τον υπάλληλο το όνομά του
onoma = input('Δώσε όνομα υπαλλήλου: ')

# Ζητάμε από τον υπάλληλο τον αρχικό του μισθό
arxikosMisthos = int(input('Δώσε μισθό: '))

# Ζητάμε από τον υπάλληλο το ποσοστό φόρου του
foros = int(input('Δώσε ποσοστό φόρου: '))

# Υπολογίζουμε τον τελικό μισθό του υπαλλήλου
telikosMisthos = arxikosMisthos - arxikosMisthos * (foros / 100)

# Εκτύπωση του ονόματος
print('Όνομα:', onoma)
# Εκτύπωση του μισθού
print('Μισθός:', telikosMisthos)
