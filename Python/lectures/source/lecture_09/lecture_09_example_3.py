# Δημιουργία συνάρτησης searchFunction
def searchFunction(pLista, key):
    # Αρχικοποίηση συνάρτησης
    counter = 0
    # Για κάθε στοιχείο της λίστας
    for i in pLista:
        # Εάν το στιγμιαίο στοιχείο της λίστας είναι ίσο με το key
        if i == key:
            # Αυξάνουμε τον counter κατά 1
            counter += 1
    # Επιστρέφει τον counter
    return counter


# Δημιουργία λιστών
lista = [[1, 2, 3, 1],
         [6, 6, 7, 8],
         [9, 1, 1, 2],
         [9, 3, 3, 6]]
searchKey = [1, 3, 6, 9]
# Δημιουργία κενής λίστας
results = []

# Για κάθε στοιχείο της λίστας searchKey
for key in searchKey:
    # Αρχικοποίηση μεταβλητής
    s = 0
    # Για κάθε υπολίστα της λίστας
    for ypolista in lista:
        # Καλούμε τη συνάρτηση searchFunction
        k = searchFunction(ypolista, key)
        # Αυξάνουμε το s κατά k
        s += k
    # Αποθηκεύουμε το s στη λίστα results
    results.append(s)

# Εκτύπωση της λίστας results
print(results)
