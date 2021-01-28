maxThesi = 0
thesi = 0

lista = [5, 7, 8, 9, 3]

for item in lista:
    if item > lista[maxThesi]:
        maxThesi = thesi
    thesi += 1

print(f"H maxThesi με τον 1ο τρόπο: {maxThesi}")

for i in range(len(lista)):
    if lista[i] > lista[maxThesi]:
        maxThesi = i

print(f"H maxThesi με τον 2ο τρόπο: {maxThesi}")
