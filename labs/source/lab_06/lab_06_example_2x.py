# Αρχικοποίηση μεταβλητών
prime = True

# Ζητάμε από το χρήστη να δώσει έναν φυσικό αριθμό
number = int(input("Δώσε έναν φυσικό αριθμό: "))

if number == 1:
    prime = False
else:
    # Για κάθε αριθμό απο το 2 εως και τον αριθμό αυτόν
    for i in range(2, number // 2 + 1):
        # Εάν βρεθεί διαιρέτης που να διαιρεί τον αριθμό
        if number % i == 0:
            # Τότε ο αριθμός δεν είναι πρώτος
            prime = False

# Εκτύπωση αποτελέσματος
if prime == True:
    print("\nO αριθμός %d είναι πρώτος αριθμός." % number)
else:
    print("\nO αριθμός %d δεν είναι πρώτος αριθμός." % number)
