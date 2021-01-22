A = [[2, 3, 4, 1],
     [7, 8, 9, 2],
     [6, 5, 1, 8],
     [1, 2, 4, 3],
     [0, 4, 7, 5]]

print(f"Η μη ταξινομημένη λίστα είναι: {A}")

for k in range(4):
    for i in range(1, 5):
        for j in range(4, i - 1, -1):
            if A[j - 1][k] > A[j][k]:
                temp = A[j - 1][k]
                A[j - 1][k] = A[j][k]
                A[j][k] = temp

print(f"Η ταξινομημένη λίστα: {A}")
