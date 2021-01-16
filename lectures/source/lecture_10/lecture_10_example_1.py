def search_function(lista_s, key):
    counter = 0
    for i in lista_s:
        if i == key:
            counter += 1
    return counter

lista = [[1, 2, 3, 1], [6, 6, 7, 8], [9, 10, 11, 12], [9, 3, 3, 16]]
search_key = [1, 3, 6, 9]
results = []

for key in search_key:
    s = 0
    for ypolista in lista:
        k = search_function(ypolista, key)
        s = s + k
    results.append(s)

print(results)
