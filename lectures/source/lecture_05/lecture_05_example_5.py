list = [3, 4, 1, 9, 4, 2]
maxThesi = 0
i = 0

while i < len(list):
    if list[i] > list[maxThesi]:
        maxThesi = i
    i += 1

print("Μέγιστη θέση:", maxThesi)
