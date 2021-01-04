# Ίδιο πλήθος γραµµών και στηλών
# Άθροισµα Διαγωνίων

sum1 = 0
sum2 = 0

for i in range(4):
    for j in range(4):
        if i == j:
            sum1 += A[i][j]
        if i + j == 3:
            sum2 += A[i][j]