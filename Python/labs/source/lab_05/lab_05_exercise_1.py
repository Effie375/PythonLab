# Αρχικοποίηση μεταβλητών
MAX_ELEMENTS = 10
thesiElaxistou = 0
thesiMegistou = 0
athroisma = 0
lista = []
even = 0
odd = 0
i = 0

# Όσο το i είναι μικρότερο του MAX_ELEMENTS
while i < MAX_ELEMENTS:
    # Ζητάμε από το χρήστη να δώσει έναν αριθμό
    number = int(input("Δώσε αριθμό: "))
    # Αποθηκεύουμε τον αριθμό στη λίστα
    lista.append(number)
    # Προσθέτουμε κάθε φορά στο athroisma τον αριθμό
    athroisma += number
    # Εάν ο αριθμός είναι ζυγός
    if number % 2 == 0:
        # Κάθε φορά προσθέτουμε στη μεταβλητη even 1
        even += 1
    # Εάν ο αριθμός είναι μονός
    if number % 2 == 1:
        # Κάθε φορά προσθέτουμε στη μεταβλητη odd 1
        odd += 1
    # Εάν βρούμε στοιχείο μεγαλύτερο απο αυτό που έχουμε μέχρι στιγμής
    if lista[i] > lista[thesiMegistou]:
        # Αποθηκεύουμε το στοιχείο που βρήκαμε στο thesiMegistou
        thesiMegistou = i
    # Εάν βρούμε στοιχείο μικρότερο απο αυτό που έχουμε μέχρι στιγμής
    if lista[i] < lista[thesiElaxistou]:
        # Αποθηκεύουμε το μικρότερο στοιχείο στο thesiElaxistou
        thesiElaxistou = i
    # Αυξάνουμε την μεταβλητή i κατά 1
    i += 1

# Υπολογίζουμε την διαφορά του max με του min
diafora = lista[thesiMegistou] - lista[thesiElaxistou]

# Εκτύπωση αποτελεσμάτων
print("\nTο άθροισμα των αριθμών είναι %d." % athroisma)
print("Tο πλήθος των περιττών είναι %d. " % odd)
print("Το πλήθος των άρτιων είναι %d." % even)
print("H διαφορά max και min είναι %d." % diafora)
