ls = [[2, 3, 4, 1],
      [7, 3, 3, 9],
      [6, 5, 5, 8],
      [1, 9, 4, 1],
      [0, 4, 7, 4]]

for j in range(4):
    sumSthlhs = 0
    for i in range(5):
        sumSthlhs += ls[i][j]
    print("Άθροισμα στήλης:", sumSthlhs)
