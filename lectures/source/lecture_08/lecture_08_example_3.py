lista = [[2, 3, 4, 1],
         [7, 3, 3, 9],
         [6, 5, 5, 8],
         [1, 9, 4, 1],
         [0, 4, 7, 4]]

megisto = lista[0][0]

for ypolista in lista:
    for item in ypolista:
        if item > megisto:
            megisto = item

print(megisto)
