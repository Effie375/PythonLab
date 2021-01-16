MATHITES = 20
TRIMHNA = 3
list = []

for i in range(MATHITES):
    list.append([])
    sum = 0
    for j in range(TRIMHNA):
        vathmos = int(input(f"Δώσε βαθμό {j+1}oυ τριμήνου: "))
        sum += vathmos
        list[i].append(vathmos)
    list[i].append(sum // TRIMHNA)    

for vathmos in range(MATHITES):
    print(f"O μέσος όρος του {vathmos+1}ου μαθητή είναι {list[vathmos][TRIMHNA]}.")
