MATHITES = 20
TRIMHNA = 3
list = []

for i in range(MATHITES):
    list.append([])
    sum = 0
    print(f"\n-------- Μαθητής {i + 1} --------")
    for j in range(TRIMHNA):
        vathmos = input(f"Δώσε βαθμό {j + 1}oυ τριμήνου: ").strip()
        # Έλεγχος ορθότητας
        while not vathmos.isdigit():
            vathmos = input("Είπα δώσε βαθμό: ").strip()
        vathmos = int(vathmos)
        sum += vathmos
        list[i].append(vathmos)
    list[i].append(sum // TRIMHNA)

print('\n', end='')

for g in range(MATHITES):
    print(f"O μέσος όρος του {g + 1}ου μαθητή είναι {list[g][TRIMHNA]}.")
