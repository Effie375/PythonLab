max_temperatures = 30
max = min = i = 0
temps = []

while i < max_temperatures:
    tem = int(input("Δώσε μια θερμοκρασία: "))
    temps.append(tem)
    i += 1

i = 0

while i < len(temps):
    if temps[i] > temps[max]:
        max = i
    elif temps[i] < temps[min]:
        min = i
    i += 1

print("Η χαμηλότερη θερμοκρασία ήταν %d βαθμούς την %d μέρα." % (temps[min],min+1))
print("Η υψηλότερη θερμοκρασία ήταν %d βαθμούς την  %d μέρα." % (temps[max],max+1))