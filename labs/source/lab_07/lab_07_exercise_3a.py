limit = int(input("Δώσε αριθμό: ").strip())

for i in range(1, limit+1):
    prime = True
    for j in range(2, i//2+1):
        if i % j == 0:
            prime = False
        if prime:
            print(i)
