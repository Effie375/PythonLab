A[[2, 3, 4, 1], [7, 8 , 19, 12], [6, 15, 10, 18], [11, 21, 24, 23], [0, -4, -7, 35]]

print("Η μη ταξινομημένη λίστα είναι:", A)

for k in range(4):
    for i in range(1,5):
        for j in range(4,i-1,-1):
            if A[j-1][k] > A[j][k]:
                temp = A[j-1][k]
                A[j-1][k] = A[j][k]
                A[j][k] = temp

print("Η ταξινομημένη λίστα:", A)
