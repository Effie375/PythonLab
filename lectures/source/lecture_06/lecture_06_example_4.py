maxThesi = 0
thesi = 0

lista = [5, 7, 8, 9, 3]

for item in lista:
    if item > lista[maxThesi]:
        maxThesi = thesi
    thesi += 1

print("H maxThesi με τον 1ο τρόπο: %d" % maxThesi)

for i in range(len(lista)):
    if lista[i] > lista[maxThesi]:
        maxThesi = i

print("H maxThesi με τον 2ο τρόπο: %d" % maxThesi)
