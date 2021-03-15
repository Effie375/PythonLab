# Δημιουργία συνάρτησης sortFunction
def sortFunction(pNames, pVathmoi):
    try:
        for i in range(len(pVathmoi) - 1):
            for j in range(len(pVathmoi) - 1, i, -1):
                if pVathmoi[j - 1] < pVathmoi[j]:
                    # Swap pVathmoi
                    temp1 = pVathmoi[j - 1]
                    pVathmoi[j - 1] = pVathmoi[j]
                    pVathmoi[j] = temp1
                    # Swap pNames
                    temp2 = pNames[j - 1]
                    pNames[j - 1] = pNames[j]
                    pNames[j] = temp2
    except:
        # Eκτύπωση κάτι πήγε στραβά
        print("Κάτι πήγε στραβά!")
        # Επιστρέφει 1
        return 1
    else:
        # Επιστρέφει 0
        return 0


# Αρχικοποίηση μεταβλητών
MAX_ELEMENTS = 200
BEST_FOITITES = 3
counter = 0
vathmoi = []
names = []

# Για όσο ο counter είναι μικρότερος από το MAX_ELEMENTS
while counter < MAX_ELEMENTS:
    # Ζητάμε από το φοιτητή να δώσει το όνομά του
    name = input("Δώσε όνομα μαθητή: ")
    # Ζητάμε από το φοιτητή να δώσει το βαθμό του
    vathmos = input("Δώσε βαθμό: ")
    # Έλεγχος ορθότητας
    while not vathmos.isdigit():
        # Ξανά ζητάμε από το φοιτητή να δώσει το βαθμό του:
        vathmos = input("Είπα δώσε βαθμό: ")
    # Μετατρέπουμε την αλφαριθμητική τιμή σε ακέραια
    vathmos = int(vathmos)
    # Αποθηκεύουμε το όνομα στη λίστα names
    names.append(name)
    # Αποθηκεύουμε το βαθμό στη λίστα vathmoi
    vathmoi.append(vathmos)
    # Αυξάνουμε τον counter κατά 1
    counter += 1


if not sortFunction(names, vathmoi):
    try:
        # Για BEST_FOITITES
        for i in range(BEST_FOITITES):
            # Εκτύπωση του καλύτερου φοιτητή
            print("Ο %dος καλύτερος είναι ο/η %s." % ((i + 1), names[i]))
    except:
        # Εκτύπωση δεν υπάρχει άλλος φοιτητής στη λίστα
        print("Δεν υπάρχει άλλος φοιτητής στη λίστα!")
