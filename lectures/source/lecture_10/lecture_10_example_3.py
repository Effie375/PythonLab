def showlist(lista_2):
    for i in range(len(lista_2)):
        lista_2[i] = lista_2[i] * 2


lista = [1, 4, 3, 5, 6]

showlist(lista[:])

print(lista)
