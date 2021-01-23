max_elements = 100
neaLista = []
lista = []
i = 0

while i < max_elements:
    num = int(input("Δώσε έναν αριθμό: "))
    lista.append(num)
    i += 1

j = len(lista)

while j > 0:
    neaLista.append(lista[j - 1])
    j -= 1

print("Η νέα λίστα είναι %s." % neaLista)
