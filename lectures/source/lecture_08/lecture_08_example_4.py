ls = [[2, 3, 4, 1], [7, 3, 3, 9], [6, 5, 5, 8], [1, 9, 4, 1], [0, 4, 7, 4]]

megistoX = 0
megistoY = 0

for x in range(len(ls)):
    for y in range(len(ls[x])):
        if ls[x][y] > ls[megistoX][megistoY]:
            megistoX = x
            megistoY = y

print(megistoX)
print(megistoY)
