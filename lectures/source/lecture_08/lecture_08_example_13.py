# Ίδιο πλήθος γραµµών και στηλών
# Άθροισµα Διαγωνίων

lista = [[2, 3, 4, 1],
     [7, 8, 9, 2],
     [6, 5, 1, 8],
     [1, 2, 4, 3],
     [0, 4, 7, 5]]

sum1 = 0
sum2 = 0

for i in range(4):
    for j in range(4):
        if i == j:
            sum1 += lista[i][j]
        if i + j == 3:
            sum2 += lista[i][j]

print(sum1, sum2)
