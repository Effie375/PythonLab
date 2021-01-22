# Διαβάζουμε από το χρήστη έναν αριθμό
number1 = int(input("Δώσε έναν αριθμό: "))

# Διαβάζουμε από το χρήστη έναν αριθμό
number2 = int(input("Δώσε έναν αριθμό: "))

# Εάν ο αριθμός 1 είναι μεγαλύτερος από τον αριθμό 2
if number1 > number2:
    # Υπολογίζουμε το άθροισμα των αριθμών
    athroisma = number1 + number2
    # Υπολογίζουμε το γινόμενο των αριθμών
    ginomeno = number1 * number2
    # Εμφανίζουμε το άθροισμα και το γινόμενο των αριθμών
    print(athroisma, ginomeno)
else:
    diafora = number1 - number2
    # Εμφανίζουμε την διαφορά των αριθμών
    print(diafora)
