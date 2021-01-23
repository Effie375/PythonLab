MATHITES = 20
TRIMHNA = 3
list = []

for i in range(MATHITES):
    list.append([])
    sum = 0
    print("\n-------- Μαθητής %d --------" % (i + 1))
    for j in range(TRIMHNA):
        vathmos = input("Δώσε βαθμό %doυ τριμήνου: " % (j + 1))
        # Έλεγχος ορθότητας
        while not vathmos.isdigit():
            vathmos = input("Είπα δώσε βαθμό: ")
        vathmos = int(vathmos)
        sum += vathmos
        list[i].append(vathmos)
    list[i].append(sum // TRIMHNA)

print('\n', end='')

for g in range(MATHITES):
    print("O μέσος όρος του %dου μαθητή είναι %d." % ((g + 1), (list[g][TRIMHNA])))
