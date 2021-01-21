lista = [3, 4, 1, 9, 7, 2]
elaxisto = lista[0]
i = 0

while i < len(lista):
    if lista[i] < elaxisto:
        elaxisto = lista[i]
    i += 1

print("Ελάχιστο:", elaxisto)
