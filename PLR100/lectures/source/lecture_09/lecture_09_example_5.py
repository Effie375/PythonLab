# Δημιουργία συνάρτησης showList
def showList(lista2):
    # Για όσο είναι το μήκος της λίστας
    for i in range(len(lista2)):
        # Πολλαπλασιάζουμε το στιγμιαίο στοιχείο της λίστας κατά 2
        lista2[i] = lista2[i] * 2


# Δημιουργία λίστας
lista = [1, 4, 3, 5, 6]

# Καλούμε τη συνάρτηση showList
showList(lista[:])

# Εκτύπωση λίστας
print(lista)
