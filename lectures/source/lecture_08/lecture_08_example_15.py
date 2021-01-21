lista1 = [[1, 2, 3],
          [1, 1, 1],
          [2, 3, 4]]
lista2 = [1, 2, 5]
lista3 = []

for key in lista2:
    counter = 0
    for ypolista in lista1:
        for i in ypolista:
            if i == key:
                counter += 1
    lista3.append(counter)

print(lista3)
