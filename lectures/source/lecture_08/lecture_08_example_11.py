A = [[2, 3, 4, 1], 
    [7, 8, 19, 12], 
    [6, 15, 10, 18], 
    [11, 21, 24, 23], 
    [0, 4, 7, 35]]

print("Η μη ταξινομημένη λίστα είναι:", A)

for k in range(5):
    for i in range(1, 4):
        for j in range(3, i - 1, -1):
            if A[k][j-1] > A[k][j]:
                temp = A[k][j - 1]
                A[k][j - 1] = A[k][j]
                A[k][j] = temp

print("Η ταξινομημένη λίστα:", A)
