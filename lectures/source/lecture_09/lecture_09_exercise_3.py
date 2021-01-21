def sort(listaP):
    for i in range(1, len(listaP)):
        for j in range(len(listaP)-1, i-1, -1):
            if listaP[j-1] > listaP[j]:
                temp = listaP[j-1]
                listaP[j-1] = listaP[j]
                listaP[j] = temp
    return listaP


list = [1, 6, 2, 5, 3, 7, 4]

print(sort(list[:]))
