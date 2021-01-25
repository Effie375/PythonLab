# Αρχικοποίηση μεταβλητών
MAX_ELEMENTS = 10
lista = []
athroisma = 0
even = 0
odd = 0
i = 0

# Όσο το i είναι μικρότερο του MAX_ELEMENTS
while i < MAX_ELEMENTS:
    # Ζητάμε από το χρήστη να δώσει έναν αριθμό
    number = int(input("Δώσε αριθμό: ").strip())
    # Αποθηκεύουμε τον αριθμό στη λίστα
    lista.append(number)
    # Προσθέτουμε κάθε φορά στο athroisma τον αριθμό
    athroisma += number
    # Εάν ο αριθμός είναι ζυγός
    if number % 2 == 0:
        # Κάθε φορά προσθέτουμε στη μεταβλητη even 1
        even += 1
    # Αλλιώς είναι μονός
    else:
        # Κάθε φορά προσθέτουμε στη μεταβλητη odd 1
        odd += 1
    # Αυξάνουμε την μεταβλητή i κατά 1
    i += 1

# Εκτύπωση αποτελεσμάτων
print(f"\nTο άθροισμα των αριθμών είναι {athroisma}.")
print(f"Tο πλήθος των περιττών είναι {odd}. ")
print(f"Το πλήθος των άρτιων είναι {even}.")

# Αρχικοποίηση μεταβλητών
megisto = 0
elaxistos = 0
i = 0

# Όσο το i είναι μικρότερο του MAX_ELEMENTS
while i < MAX_ELEMENTS:
    # Εάν βρούμε στοιχείο μεγαλύτερο απο αυτό που έχουμε μέχρι στιγμής
    if lista[i] > lista[megisto]:
        # Αποθηκεύουμε το στοιχείο που βρήκαμε στο megisto
        megisto = i
    # Αλλιώς εάν βρούμε στοιχείο μικρότερο απο αυτό που έχουμε μέχρι στιγμής
    elif lista[i] < lista[elaxistos]:
        # Αποθηκεύουμε το μικρότερο στοιχείο στο elaxistos
        elaxistos = i
    # Αυξάνουμε την μεταβλητή i κατά 1
    i += 1

# Υπολογίζουμε την διαφορά του max με του min
diafora = lista[megisto] - lista[elaxistos]

# Εκτύπωση αποτελέσματος
print(f"H διαφορά max και min είναι {diafora}.")
