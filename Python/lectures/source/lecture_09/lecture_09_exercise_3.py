# Δημιουργία συνάρτησης sort
def sort(listaP):
    for i in range(1, len(listaP)):
        for j in range(len(listaP) - 1, i - 1, -1):
            if listaP[j - 1] > listaP[j]:
                # Swap listaP
                temp = listaP[j - 1]
                listaP[j - 1] = listaP[j]
                listaP[j] = temp
    # Επιστρέφει τη listaP
    return listaP


# Δημιουργία λίστας
lista = [1, 6, 2, 5, 3, 7, 4]

# Καλούμε τη συνάρτηση sort και εκτύπωνουμε
print(sort(lista[:]))
