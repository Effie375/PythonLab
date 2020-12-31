plithos = 0

num = float(input("Δώσε αριθμό: "))

while num != 0:
    if num > 0:
        plithos += 1
        num = float(input("Δώσε αριθμό: "))

if plithos > 0:
    print("Θετικοί:", plithos)
else:
    print ("Δεν υπάρχουν θετικοί :(")
