lista = [5, 7, 8, 9, 3]

megisto = lista[0]
elaxisto = lista[0]

for item in lista:
    if item > megisto:
        megisto = item

for item in lista:
    if item < elaxisto:
        elaxisto = item

print("Μέγιστο: %d" % megisto)
print("Ελάχιστο: %d" % elaxisto)
