vath = []
sum = 0

for i in range(200):
    num = int(input("Δώσε βαθμό: ").strip())
    vath.append(num)
    sum += num

mo = sum / 200

for i in range(200):
    if vath[i] > mo:
        print(i)
