def searchFunction(listaS, key):
    counter = 0
    for i in listaS:
        if i == key:
            counter += 1
    return counter


lista = [[1, 2, 3, 1], 
    [6, 6, 7, 8], 
    [9, 10, 11, 12], 
    [9, 3, 3, 16]]
searchKey = [1, 3, 6, 9]
results = []

for key in searchKey:
    s = 0
    for ypolista in lista:
        k = searchFunction(ypolista, key)
        s = s + k
    results.append(s)

print(results)
