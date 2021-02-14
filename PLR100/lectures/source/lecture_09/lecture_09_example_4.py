# Δημιουργία συνάρτησης athroisma
def athroisma(listaNew):
    # Για κάθε στοιχείο της λίστας
    for item in listaNew:
        item.sort(reverse=True)


# Δημιουργία λίστας
lista = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 1, 1, 2],
         [3, 4, 5, 6]]

# Για κάθε στοιχείο της λίστας
for item in lista:
    # Εκτύπωση το στιγμιαίο στοιχείο της λίστας
    print(item)

# Καλούμε τη συνάρτηση lista
athroisma(lista)

# Εκτύπωση διαχωριστικό ....
print("...........")

# Για κάθε στοιχείο της λίστας
for item in lista:
    # Εκτύπωση το στιγμιαίο στοιχείο της λίστας
    print(item)
