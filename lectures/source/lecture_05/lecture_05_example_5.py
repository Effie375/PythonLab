lista = [3, 4, 1, 9, 4, 2]
maxThesi = 0
i = 0

while i < len(lista):
    if lista[i] > lista[maxThesi]:
        maxThesi = i
    i += 1

print(f"Μέγιστη θέση: {maxThesi}")
