# Bubble Sort

ls = [5, 4, 3, 2, 1]

for j in range(4):
    for i in range(4, j, -1):
        if ls[i-1] > ls[i]:
            temp = ls[i-1]
            ls[i-1] = ls[i]
            ls[i] = temp
    print(ls)
