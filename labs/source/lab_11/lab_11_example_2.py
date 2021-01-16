def sort(A):
    for i in range(1, len(A)):
        for j in range(len(A)-1, 0, -1):
            if A[j-1] > A[j]:
                temp = A[j-1]
                A[j-1] = A[j]
                A[j] = temp
    return A

list = [5, 7, 8, 9, 3]

x = sort(list[:])
print(x)