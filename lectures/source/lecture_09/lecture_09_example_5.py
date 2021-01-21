def showList(lista2):
    for i in range(len(lista2)):
        lista2[i] = lista2[i] * 2


lista = [1, 4, 3, 5, 6]

showList(lista[:])

print(lista)
