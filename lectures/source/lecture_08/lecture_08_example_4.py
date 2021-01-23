lista = [[2, 3, 4, 1],
         [7, 3, 3, 9],
         [6, 5, 5, 8],
         [1, 9, 4, 1],
         [0, 4, 7, 4]]

megistoX = 0
megistoY = 0

for x in range(len(lista)):
    for y in range(len(lista[x])):
        if lista[x][y] > lista[megistoX][megistoY]:
            megistoX = x
            megistoY = y

print(megistoX)
print(megistoY)
