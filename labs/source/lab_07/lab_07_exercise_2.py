arithmoi = []

for i in range(10):
    arithmoi.append(int(input("Δώσε αριθμό: ")))

num = int(input("Δώσε αριθμό για έλεγχο διαιρετέων: "))

for i in arithmoi:
    if i % num == 0:
        print(i)
