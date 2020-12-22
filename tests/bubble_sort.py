import random


def swap(list, j):
    temp = list[j-1]
    list[j-1] = list[j]
    list[j] = temp
    return list


A = [random.randint(0, 100) for x in range(random.randint(10, 20))]

print(A)

for i in range(len(A)):
    for j in range(len(A)-1,i,-1):
        if A[j-1] > A[j]:
            A = swap(A,j)

print(A)

mikos = len(A)//2

if len(A)%2 == 0:
    a = A[mikos-1]
    b = A[mikos]
    diamesos = (a+b)/2
else:
    diamesos = A[mikos]

print("diamesos:", diamesos)
