sum = 0
ls = []

for i in range(7):
    vathmos = int(input("Δώσε βαθμό: "))
    ls.append(vathmos)

k = 1

for i in ls:
    i = i * 5 * k
    k = k + 1
    um = sum + i
mo = sum / 7

print("Ο μέσος όρος είναι", mo)

"""
Εναλλακτικά
k = 5
for i in ls:
    i = i * k
    k = k + 5
    sum = sum + i
"""
