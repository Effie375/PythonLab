counter = 0

num = int(input("Δώσε έναν αριθμό: ").strip())

while num != 0:
    if num % 2:
        counter += 1
    num = int(input("Δώσε έναν αριθμό: ").strip())

print(f"Οι περιττοί αριθμοί είναι {counter}.")
