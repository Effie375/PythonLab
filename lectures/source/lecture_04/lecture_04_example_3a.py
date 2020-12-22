sum = num = 0
key = 55555

while num != key:
    sum += num
    num = int(input("Δώσε έναν αριθμό: ").strip())

print(f"Το άθροισμα είναι {sum}")