# Εισαγωγή δεδομένων
limit = int(input("Δώσε αριθμό: "))

for i in range(1, limit + 1):
    prime = True
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            prime = False
        if prime:
            # Εκτύπωση αποτελέσματος
            print(i)
