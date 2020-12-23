list = []

for i in range(10):
    list.append(int(input("Δώσε αριθμό: ")))

num = int(input("Δώσε αριθμό για έλεγχο διαιρετέων: "))

for arithmos in list:
    if arithmos % num == 0:
        print(arithmos)
