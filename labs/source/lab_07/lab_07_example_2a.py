prime = True

number = int(input("Δώσε αριθμό: ").strip())

for i in range(2, number // 2 + 1):
    if number % i == 0:
        prime = False

print(prime)
