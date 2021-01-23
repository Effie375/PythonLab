lista = [[2, 3, 4, 1],
         [7, 3, 3, 9],
         [6, 5, 5, 8],
         [1, 9, 4, 1],
         [0, 4, 7, 4]]

key = int(input("Δώσε στοιχείο που αναζητάς: "))

found = False
i = 0
j = 0

while i < 5 and not found:
    while j < 4 and not found:
        if key == lista[i][j]:
            print(i, j)
            found = True
        j += 1
    j = 0
    i += 1
