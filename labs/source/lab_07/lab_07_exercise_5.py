fib_no = input("Δώσε αριθμό Fibonacci:")
while not fib_no.isdigit():
    fib_no = input("Δώσε σωστό αριθμό Fibonacci:")

fib_no = int(fib_no)

fib_minus_2 = 0
fib_minus_1 = 1

if fib_no == 1:
    fib = 1
elif fib_no == 0:
    fib = 0
else:
    for i in range(fib_no-1):
        fib = fib_minus_1 + fib_minus_2
        fib_minus_2 = fib_minus_1
        fib_minus_1 = fib

print(fib)
