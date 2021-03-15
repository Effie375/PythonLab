# Δημιουργία συνάρτησης sunolo
def sunolo(x, y):
    # Υπολογίζουμε το άθροισμα των δύο παραμέτρων
    athroisma = x + y
    # Επιστρέφει το άθροισμα
    return athroisma


# Δημιουργία συνάρτησης sayHello
def sayHello():
    # Εκτύπωση Hello
    print("Hello")
# Δεν επιστρέφει κάτι άρα δε χρειάζεται return


# -------main--------
# Αρχικοποίηση μεταβλητών
x = 3
y = 4

# Καλόυμε τη συνάρτηση sunolo
athroisma = sunolo(x, y)
# Εκτύπωση το άθροισμα
print(athroisma)

# Καλόυμε τη συνάρτηση sayHello
sayHello()
