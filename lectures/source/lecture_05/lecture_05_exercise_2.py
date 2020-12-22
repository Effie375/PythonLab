vath = []
i = 0
sum = 0

while i < 200:
    num = int(input("Δώσε βαθμό: "))
    vath.append(num)
    sum += vath[i]
    i += 1

mo = sum / 200
i = 0

while i < 200:
    if vath[i] > mo:
        print(i)
    i += 1
