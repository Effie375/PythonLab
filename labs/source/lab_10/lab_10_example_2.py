# Δημιουργία συνάρτησης sort
def sort(listaP):
    for i in range(1, len(listaP)):
        for j in range(len(listaP) - 1, 0, -1):
            if listaP[j - 1] > listaP[j]:
                # Swap listaP
                temp = listaP[j - 1]
                listaP[j - 1] = listaP[j]
                listaP[j] = temp
    # Eπιστροφή listaP στη main
    return listaP

# Δημιουργία λίστας
list = [5, 7, 8, 9, 3]

x = sort(list[:])
print(x)
