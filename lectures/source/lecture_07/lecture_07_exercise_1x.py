# Δημιουργία συνάρτησης sortFunction
def sortFunction(plist):
    try:
        for index in range(len(plist) - 1):
            for j in range(len(plist) - 1, index, -1):
                if plist[j - 1] > plist[j]:
                    # Swap plist
                    temp = plist[j - 1]
                    plist[j - 1] = plist[j]
                    plist[j] = temp
    except:
        # Εκτύπωση κάτι πήγε στραβά
        print("Κάτι πήγε στραβά!")
        # Επιστρέφει 1
        return 1
    else:
        # Επιστρέφει 0
        return 0


# Αρχικοποίηση μεταβλητών
MAX_NUMBERS = 100
lista = []

# Για MAX_NUMBERS
for i in range(MAX_NUMBERS):
    # Ζητάμε από το χρήστη να δώσει αριθμό
    num = input("Δώσε αριθμό: ").strip()
    # Έλεγχος ορθότητας
    while not num.isdigit():
        # Ξανά ζητάμε από το χρήστη να δώσει αριθμό
        num = input("Είπα δώσε αριθμό: ").strip()
    # Μετατρέπουμε την αλφαριθμητική τιμή σε ακέραια
    num = int(num)
    # Αποθηκεύουμε τον αριθμό στη λίστα
    lista.append(num)

if not sortFunction(lista):
    # Εκτύπωση του μεγαλύτερου αριθμού της λίστας
    print(f"\nΟ μεγαλύτερος αριθμός είναι το {lista[len(lista) - 1]}.")
    # Εκτύπωση του μικρότερου αριθμού της λίστας
    print(f"Ο μικρότερος αριθμός είναι το {lista[0]}.")
