lista = [5,7,8,9,3]
elaxisto = lista[0]
megisto = lista[0]
i = 0

while i < len(lista):
    if lista[i] > megisto:
        megisto = lista[i]
    i += 1

print(f"Ο μέγιστος αριθμός είναι το: {megisto}")

i = 0

while i < len(lista):
    if lista[i] < elaxisto:
        elaxisto = lista[i]
    i += 1

print(f"Ο ελάχιστος αριθμός είναι το: {elaxisto}")