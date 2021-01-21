# Αρχικοποίηση μεταβλητής
alfabito = "abcdefghijklmnopqrstuvwxyz"

# Ζητάμε από το χρήστη να δώσει μια λέξη
leksi = input("Δώσε λέξη με λατινικούς χαρακτήρες: ").lower().strip()

# Για κάθε γράμμα του λατινικού αλφαβήτου
for gramma in alfabito:
    # Αρχικοποιήση του μετρητή
    counter = 0
    # Για κάθε γράμμα της λέξης
    for grammaLeksis in leksi:
        # εάν το γράμμα της λέξης είναι ίσο με το στιγμιαίο γράμμα
        if grammaLeksis == gramma:
            # Αυξάνουμε το μετρητή κατά 1
            counter += 1
    # εάν ο μετρητής είναι 1
    if counter == 1:
        print(f"To γράμμα '{gramma}' εμφανίστηκε {counter} φορά.")
    # Αλλιώς εάν ο μετρητής δεν είναι ο΄΄ύτε 0 αλλά ο΄΄ύτε 1
    elif counter != 0:
        print(f"To γράμμα '{gramma}' εμφανίστηκε {counter} φορές.")
