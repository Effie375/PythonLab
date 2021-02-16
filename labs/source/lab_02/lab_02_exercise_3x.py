import datetime

# Ζητάμε από το χρήστη να δώσει το όνομα του
onoma = input("Ποιο είναι το όνομα σου: ").strip()

# Ζητάμε από το χρήστη να δώσει την ηλικία του
ilikia = input("Ποια είναι η ηλικία σου: ").strip()

# Μετατροπή από str σε int
ilikia = int(ilikia)

# Η βιβλιοθήκη datetime βρίσκει το τωρινό έτος
twrinoEtos = datetime.datetime.today().year

# Υπολογισμός έτους γέννησης
etosGennhshs = twrinoEtos - ilikia

# Υπολογισμός χρονιάς που θα γίνει 100
ekatoXronwn = etosGennhshs + 100

# Εάν το όνομα τελειώνει σε 'ς' ή 's'
if (onoma[-1] == 's') or (onoma[-1] == 'ς'):
    # Σβήσε το τελευταίο γράμμα
    onoma = onoma[:-1]

# Κάνε το πρώτο γράμμα κεφαλαίο
onoma = onoma[0].upper() + onoma[1:]

# Εκτύπωση αποτελέσματος
print(f"{onoma} θα γίνεις 100 το έτος {ekatoXronwn}.")
