lista = [[2, 3, 4, 1],
    [7, 8, 9, 2],
    [6, 5, 1, 8],
    [1, 2, 4, 3],
    [0, 4, 7, 5]]

print("Η μη ταξινομημένη λίστα είναι:", lista)

for k in range(4):
    for i in range(1, 5):
        for j in range(4, i-1, -1):
            if lista[j-1][k] > lista[j][k]:
                temp = lista[j-1][k]
                lista[j-1][k] = lista[j][k]
                lista[j][k] = temp

print("Η ταξινομημένη λίστα:", lista)
