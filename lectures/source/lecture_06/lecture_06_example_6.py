lista = [3, 4, 1, 9, 4, 2]
maxThesi = 0

for i in range(len(lista)):
    if lista[i] > lista[maxThesi]:
        maxThesi = i

print("Μέγιστη θέση:", maxThesi)
