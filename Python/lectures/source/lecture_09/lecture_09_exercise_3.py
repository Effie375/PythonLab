# Δημιουργία συνάρτησης sort
def sort(pList):
    for i in range(1, len(pList)):
        for j in range(len(pList) - 1, i - 1, -1):
            if pList[j - 1] > pList[j]:
                # Swap pList
                temp = pList[j - 1]
                pList[j - 1] = pList[j]
                pList[j] = temp
    # Επιστρέφει τη pList
    return pList


# Δημιουργία λίστας
lista = [1, 6, 2, 5, 3, 7, 4]

# Καλούμε τη συνάρτηση sort και εκτύπωνουμε
print(sort(lista[:]))
