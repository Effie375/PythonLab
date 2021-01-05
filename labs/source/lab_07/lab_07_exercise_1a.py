sum = 0
ls = []
max_elements = 7

for i in range(max_elements):
    vathmos = int(input("Δώσε βαθμό: ").strip())
    ls.append(vathmos)

k = 1

for i in ls:
    i = i * 5 * k
    k = k + 1
    um = sum + i

mo = sum / 7

print(f"Ο μέσος όρος είναι {mo}")
