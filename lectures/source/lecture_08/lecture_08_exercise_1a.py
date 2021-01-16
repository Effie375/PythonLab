TRIMINA = 3
list = []
upoloista = []
sum = 0

for i in range(2):
    upoloista = []
    for x in range(TRIMINA):
        vathmos = int(input(f"Δώσε βαθμό {x+1}oυ τριμήνου: "))
        sum += vathmos
        upoloista.append(vathmos)
    upoloista.append(sum // TRIMINA)
    list.append(upoloista)

for mo in range(2):
    print(f"O μέσος όρος του {mo+1}ου μαθητή είναι {list[mo][TRIMINA]}.")
