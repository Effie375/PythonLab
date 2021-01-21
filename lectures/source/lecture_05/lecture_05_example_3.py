lista = [1, 4, 6, 9, 7, 2]

megisto = lista[0]
i = 0

while i < len(lista):
    if lista[i] > megisto:
        megisto = lista[i]
    i += 1

print("Μέγιστο:", megisto)
