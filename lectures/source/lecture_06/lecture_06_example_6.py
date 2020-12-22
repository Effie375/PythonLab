list = [3, 4, 1, 9, 4, 2]
maxThesi = 0

for i in range(len(list)):
    if list[i] > list[maxThesi]:
        maxThesi = i

print("Μέγιστη θέση:", maxThesi)
