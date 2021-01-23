# Αρχικοποιούμε τις μεταβλητές
total = 0
i = 0

# Όσο το i είναι μικρότερο του  6
while i < 6:
    # Ζητάμε από το χρήστη να δώσει έναν βαθμό
    vathmos = input("Δώσε βαθμό (int): ").strip()
    while not vathmos.isdigit():
        # Ζητάμε από το χρήστη να δώσει έναν σωστό βαθμό
        vathmos = input("Δώσε έναν ακέραιο βαθμό: ").strip()
    # Μετατρέπουμε τον βαθμό σε πραγματική τιμή
    vathmos = float(vathmos)
    # Προσθέτουμε στην μεταβλητή total τον βαθμό
    total += vathmos
    # Αυξάνουμε την μεταβλητή i κατά 1
    i += 1

# Υπολογίζουμε το μέσο όρο
mo = total / 6

# εάν ο μέσος όρος είναι μεγαλύτερος του 10
if mo > 10:
    print("Κάτι δεν πάει καλά...")
# Αλλιώς εάν ο μέσος όρος είναι μεγαλύτερος ή ίσος του 8.5
# και μικρότερος ή ίσος του 10
elif mo >= 8.5:
    print(f"Άριστα με μέσο όρο {mo:.1f}!")
# Αλλιώς εάν ο μέσος όρος είναι μεγαλύτερος ή ίσος του 6.5
# και μικρότερος του 8.5
elif mo >= 6.5:
    print(f"Λίαν Καλώς με μέσο όρο {mo:.1f}")
# Αλλιώς εάν ο μέσος όρος είναι μεγαλύτερος ή ίσος του 5
# και μικρότερος του 6.5
elif mo >= 5:
    print(f"Καλώς με μέσο όρο {mo:.1f}")
# Αλλιώς εμφάνισε μήνυμα ότι ο χρήστης κόπηκε
else:
    print("Kόπηκες")
