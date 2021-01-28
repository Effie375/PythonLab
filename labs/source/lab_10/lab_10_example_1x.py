# Δημιουργία συνάρτησης readAndCheck
def readAndCheck():
    # Αρχικοποίηση μεταβλητής
    good = True
    # Για όσο το good είναι True
    while good:
        # Ζητάμε από το χρήστη να δώσει αριθμό
        num = input("Δώσε αριθμό: ").strip()
        # Κάνουμε έλεγχο ορθότητας
        while not num.isdigit():
            # Ζητάμε από το χρήστη να δώσει σωστά τον αριθμό
            num = input("Δώσε αριθμό: ").strip()
        # Μετατρέπουμε τον αριθμό σε ακέραιο
        num = int(num)
        # Εάν ο αριθμός είναι μεγαλύτερο η ίσος από το 0 ή μικρότερος ή ίσος από το 10
        if 0 <= num <= 10:
            # Το good γίνεται False
            good = False
    # Επιστρέφει το num
    return num
