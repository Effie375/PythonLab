lista = [[2, 3, 4, 1],
         [7, 3, 3, 9],
         [6, 5, 5, 8],
         [1, 9, 4, 1],
         [0, 4, 7, 4]]

for ypolista in lista:
    sumGrammhs = 0
    for item in ypolista:
        sumGrammhs += item

    print(f"Άθροισμα γραμμής: {sumGrammhs}")
