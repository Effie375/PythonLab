def athroisma(listaNew):
    for item in listaNew:
        item.sort(reverse=True)


lista = [[1, 2, 3, 4], 
         [5, 6, 7, 8], 
         [9, 1, 1, 2], 
         [3, 4, 5, 6]]

for item in lista:
    print(item)

athroisma(lista)

print("...........")

for item in lista:
    print(item)
