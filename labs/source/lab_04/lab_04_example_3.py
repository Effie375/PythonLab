# Αρχικοποιούμε τις μεταβλητές
i = 0
synolo = 0

# Όσο το i είναι μικρότερο του 10
while i < 10:
    # Ζητάμε από το χρήστη να δώσει έναν αριθμό
    number = input("Δώσε αριθμό (int): ").strip()
    # Κάνουμε έλεγχο ορθότητας
    while not number.isdigit():
        # Ζητάμε από το χρήστη να δώσει σωστά τον αριθμό
        number = input("Είπα δώσε ακέραιο αριθμό: ").strip()
    # Μετατρέπουμε τον αριθμό σε ακέραιο
    number = int(number)
    # Προσθέτουμε στην μεταβλητή synolo τον αριθμό
    synolo = synolo + number
    # Αυξάνουμε την μεταβλητή i κατά 1
    i = i + 1

# Εκτυπώνουμε το αποτέλεσμα
print(f"Το σύνολο είναι: {synolo}")
