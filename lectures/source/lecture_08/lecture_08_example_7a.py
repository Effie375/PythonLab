ls = [[2, 3, 4, 1], [7, 3, 3, 9], [6, 5, 5, 8], [1, 9, 4, 1], [0, 4, 7, 4]]

for ypolista in ls:
    megistoGrammhs = ypolista[0]
    for i in ypolista:
        if megistoGrammhs < i:
            megistoGrammhs = i
    print(f"Μέγιστο γραμμής: {megistoGrammhs}")
