def dinami(var):
    var *= var
    return var


key = int(input("Δώσε αριθμό: ").strip())
sum = 0

for i in range(1, key + 1):
    var = dinami(i)
    sum += var

print(sum)
