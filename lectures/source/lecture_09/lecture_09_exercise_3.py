def sort(A):
    for i in range(1, len(A)):
        for j in range(len(A)-1, i-1, -1):
            if A[j-1] > A[j]:
                temp = A[j-1]
                A[j-1] = A[j]
                A[j] = temp
    return A


list = [1, 6, 2, 5, 3, 7, 4]

print(sort(list[:]))
