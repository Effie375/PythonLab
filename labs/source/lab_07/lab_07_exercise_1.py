sum = 0
l = []

for i in range(7):
    vathmos=int(input("Δώσε βαθμό: "))
    l.append(vathmos)

k = 1 

for i in l: 
    i = i * 5 * k 
    k = k + 1 
    um = sum + i 
mo = sum / 7

print("Ο μέσος όρος είναι", mo)

# Εναλλακτικά k = 5
# for i in l:
    # i = i * k
    # k = k + 5
    # sum = sum + i
