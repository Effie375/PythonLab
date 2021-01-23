lista = [5, 7, 8, 9, 3]

print("Η λίστα μας πριν τη ταξινόμηση είναι: %s" % lista)

for i in range(len(lista)):
    for j in range(len(lista) - 1, i, -1):
        if lista[j - 1] > lista[j]:
            temp = lista[j - 1]
            lista[j - 1] = lista[j]
            lista[j] = temp

print("Η λίστα μας μετά τη ταξινόμηση είναι: %s" % lista)
