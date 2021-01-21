# Εισαγωγή δεδομένων
fibNo = input("Δώσε αριθμό Fibonacci:")

while not fibNo.isdigit():
    # Εισαγωγή δεδομένων
    fibNo = input("Δώσε σωστό αριθμό Fibonacci:")

# Μετατροπή από str σε int
fibNo = int(fibNo)

# Αρχικοποίηση μεταβλητών
fibMinus2 = 0
fibMinus1 = 1

if fibNo == 1:
    fib = 1
elif fibNo == 0:
    fib = 0
else:
    for i in range(fibNo - 1):
        fib = fibMinus1 + fibMinus2
        fibMinus2 = fibMinus1
        fibMinus1 = fib

# Εκτύπωση αποτελέσματος
print(fib)
