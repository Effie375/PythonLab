# Αρχικοποίηση μεταβλητών
MAX_AKSIA = 3000
weeks = 0
dosi = 20
tameio = 0

# Για όσο το ταμείο είναι μικρότερο ή ίσο από την MAX_AKSIA
while tameio <= MAX_AKSIA:
    # Αυξάνουμε το ταμείο κατά δόση
    tameio += dosi
    # Αυξάνουμε τη μεταβλητή weeks κατά 1
    weeks += 1
    # Πολλαπλασιάζουμε τη δόση κάθε φορά με το 2
    dosi *= 2

# Εκτύπωση τις εβδομάδες
print(weeks)

# Εάν το ταμείο είναι μεγαλύτερη από την MAX_AKSIA
if tameio > MAX_AKSIA:
    # Εκτύπωση πόσα ευρώ περίσσεψαν
    print(f"Περίσσεψαν {tameio - MAX_AKSIA} Ευρώ.")
