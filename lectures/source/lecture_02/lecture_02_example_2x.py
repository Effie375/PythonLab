# Διαβάζουμε από τον υπάλληλο το όνομα του
onoma = input('Δώσε όνομα υπαλλήλου: ')

# Διαβάζουμε από τον υπάλληλο τον αρχικό του μισθό
arxikosMisthos = int(input('Δώσε μισθό: '))

# Διαβάζουμε από τον υπάλληλο το ποσοστό φόρου του
foros = int(input('Δώσε ποσοστό φόρου: '))

# Υπολογίζουμε τον τελικό μισθό του υπαλλήλου
telikosMisthos = arxikosMisthos - arxikosMisthos * (foros / 100)

# Εμφανίζουμε το όνομα του υπαλλήλου και τον τελικό μισθό του
print('Όνομα: %s' % onoma)
print('Μισθός: %.2f' % telikosMisthos)
