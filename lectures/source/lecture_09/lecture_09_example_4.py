def athroisma(lista_new):
    for item in lista_new:
        item.sort(reverse=True)


lista = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

for item in lista:
    print(item)

athroisma(lista)

print("...........")

for item in lista:
    print(item)
