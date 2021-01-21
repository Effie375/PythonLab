ls = [[1, 2, 3], [1, 1, 1], [2, 3, 4]]
lista1 = [1, 2, 5]
lista2 = []

for key in lista1:
    counter = 0
    for ypolista in ls:
        for i in ypolista:
            if i == key:
                counter += 1
    lista2.append(counter)

print(lista2)
