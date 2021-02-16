# Δημιουργία συνάρτησης readAndCheck
def readAndCheck():
    # Αρχικοποίηση μεταβλητής
    good = True
    # Για όσο το good είναι True
    while good:
        # Ζητάμε από το χρήστη να δώσει αριθμό
        num = input("Δώσε αριθμό: ")
        # Κάνουμε έλεγχο ορθότητας
        while not num.isdigit():
            # Ζητάμε από το χρήστη να δώσει σωστά τον αριθμό
            num = input("Δώσε αριθμό: ")
        # Μετατρέπουμε τον αριθμό σε ακέραιο
        num = int(num)
        # Εάν ο αριθμός είναι μεγαλύτερο η ίσος από το 0 ή μικρότερος ή ίσος από το 10
        if 0 <= num <= 10:
            # Το good γίνεται False
            good = False
    # Επιστρέφει το num
    return num


# Δημιουργία συνάρτησης sort
def sort(listP):
    """ Αυτή η συνάρτηση ταξινομεί τη λίστα κατά αύξουσα σειρά."""
    for i in range(1, len(listP)):
        for j in range(len(listP) - 1, 0, -1):
            if listP[j - 1] > listP[j]:
                # Swap listP
                temp = listP[j - 1]
                listP[j - 1] = listP[j]
                listP[j] = temp
    # Επιστρέφει το listP
    return listP


# Δημιουργία συνάρτησης readMarks
def readMarks():
    # Δηνιουργία κενής λίστας
    vathmoi = []
    # Για 10 φορές
    for i in range(10):
        # Αποθηκεύουμε στη λίστα vathmoi στα στοιχεία που θα πάρουμε από τη συνάρτηση readAndCheck
        vathmoi.append(readAndCheck())
    # Επιστρέφει το vathmoi
    return vathmoi


# Αρχικοποίηση μεταβλητής
MAX_ELEMENTS = 10

# Για MAX_ELEMENTS
for i in range(MAX_ELEMENTS):
    # Καλούμε τη συνάρτηση readMarks
    vathmoi = readMarks()
    # Εκτύπωση της ταξινομημένης λίστας
    print(sort(vathmoi))
