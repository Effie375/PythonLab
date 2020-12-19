max_temperatures = 30
max = min = i = 0
temps = []

while i < max_temperatures:
    tem = int(input("Δώσε μια θερμοκρασία: ").strip())
    temps.append(tem)
    i += 1

i = 0

while i < len(temps):
    if temps[i] > temps[max]:
        max = i
    elif temps[i] < temps[min]:
        min = i
    i += 1

print(f"Η χαμηλότερη θερμοκρασία ήταν {temps[min]} βαθμούς την {min+1} μέρα.")
print(f"Η υψηλότερη θερμοκρασία ήταν {temps[max]} βαθμούς την  {max+1} μέρα.")