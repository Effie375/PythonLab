# Ζητάμε από το χρήστη να δώσει τον νιοστό όρο Fibonacci
fibNo = input("Δώσε νιοστό όρο Fibonacci (int): ").strip()

# Όσο ο νιοστός όρος δεν είναι αριθμός
while not fibNo.isdigit():
    # Ζητάμε από το χρήστη να δώσει σωστό νιοστό όρο Fibonacci
    fibNo = input("Δώσε έναν ακέραιο νιοστό όρο Fibonacci: ").strip()

# Μετατρέπουμε τον νιοστό όρο σε ακέραιο αριθμό
fibNo = int(fibNo)

# Αρχικοποίηση μεταβλητών
fibMinus2 = 0
fibMinus1 = 1

# Εάν ο νιοστός όρος Fibonacci είναι 1
if fibNo == 1:
    fib = 1
# Αλλιώς εάν ο νιοστός όρος Fibonacci είναι 0
elif fibNo == 0:
    fib = 0
# Αλλιώς εάν ο νιοστός όρος Fibonacci δεν είναι ούτε 0 ούτε 1
else:
    # Για κάθε νιοστό αριθμό - 1
    for i in range(fibNo - 1):
        # Ο αριθμός Fibonacci προκύπτει από το άθροισμα του ν-1 και ν-2
        fib = fibMinus1 + fibMinus2
        # Ο ν-2 όρος είναι ο ν-1
        fibMinus2 = fibMinus1
        # Ο ν-1 είναι ο αριθμός Fibonacci
        fibMinus1 = fib

# Εκτύπωση νιοστού αριθμού Fibonacci
print(fib)
