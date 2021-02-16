# Ζητάμε από τον υπάλληλο το όνομά του
onoma = input('Δώσε όνομα υπαλλήλου: ').strip()

# Ζητάμε από τον υπάλληλο τον αρχικό του μισθό
arxikosMisthos = int(input('Δώσε μισθό: ').strip())

# Ζητάμε από τον υπάλληλο το ποσοστό φόρου του
foros = int(input('Δώσε ποσοστό φόρου: ').strip())

# Υπολογίζουμε τον τελικό μισθό του υπαλλήλου
telikosMisthos = arxikosMisthos - arxikosMisthos * (foros / 100)

# Εκτύπωση του ονόματος
print(f'Όνομα: {onoma}')
# Εκτύπωση του μισθού
print(f'Μισθός: {telikosMisthos}')
