def square(n):
    n = n * n

    return n


athroisma = 0
number = int(input("Δώσε αριθμό: "))

for i in range (number + 1):
    athroisma += square(i)

print("Το άθροισμα των αριθμών είναι:", athroisma)
