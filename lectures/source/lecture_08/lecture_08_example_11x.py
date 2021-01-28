lista = [[2, 3, 4, 1],
         [7, 8, 9, 2],
         [6, 5, 1, 8],
         [1, 2, 4, 3],
         [0, 4, 7, 5]]

print(f"Η μη ταξινομημένη λίστα είναι: {lista}")

for k in range(5):
    for i in range(1, 4):
        for j in range(3, i - 1, -1):
            if lista[k][j - 1] > lista[k][j]:
                temp = lista[k][j - 1]
                lista[k][j - 1] = lista[k][j]
                lista[k][j] = temp

print(f"Η ταξινομημένη λίστα: {lista}")
