# Διαβάζουμε από τον υπάλληλο το όνομα του
onoma = input('Δώσε όνομα υπαλλήλου: ').strip()

# Διαβάζουμε από τον υπάλληλο τον αρχικό του μισθό
arxikosMisthos = int(input('Δώσε μισθό: ').strip())

# Διαβάζουμε από τον υπάλληλο το ποσοστό φόρου του
foros = int(input('Δώσε ποσοστό φόρου: ').strip())

# Υπολογίζουμε τον τελικό μισθό του υπαλλήλου
telikosMisthos = arxikosMisthos - arxikosMisthos * (foros / 100)

# Εμφανίζουμε το όνομα του υπαλλήλου και τον τελικό μισθό του
print(f'Όνομα: {onoma}')
print(f'Μισθός: {telikosMisthos}')
