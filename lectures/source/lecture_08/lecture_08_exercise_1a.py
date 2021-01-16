MATHITES = 20
TRIMHNA = 3
list = []

for i in range(MATHITES):
    list.append([])
    sum = 0
    for j in range(TRIMHNA):
        vathmos = int(input(f"Δώσε βαθμό {j+1}oυ τριμήνου: ").strip())
        sum += vathmos
        list[i].append(vathmos)
    list[i].append(sum // TRIMHNA)

for g in range(MATHITES):
    print(f"O μέσος όρος του {g+1}ου μαθητή είναι {list[g][TRIMHNA]}.")
