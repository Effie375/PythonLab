# Διαβάζουμε από το χρήστη έναν αριθμό
number1 = float(input("Δώσε έναν αριθμό: "))

# Διαβάζουμε από το χρήστη έναν αριθμό
number2 = float(input("Δώσε έναν αριθμό: "))

# Διαβάζουμε από το χρήστη έναν αριθμό
number3 = float(input("Δώσε έναν αριθμό: "))

# Υπολογίζουμε το άθροισμα των αριθμών αυτών
sum = number1 + number2 + number3

# Εάν το άθροισμα είναι μεγαλύτερο από 100
if sum > 100:
    # Υπολογίζουμε το γινόμενο των δύο πρώτων αριθμών
    ginomeno = number1 * number2
    print("Το γινόμενο ισούται με %.2f." % ginomeno)
else:
    # Υπολογίζουμε την απόλυτη τιµή της διαφοράς των δύο τελευταίων
    diafora = number2 - number3
    print("Η διαφορά των αριθμών σε απόλυτη τιμή είναι %d ." % abs(diafora))
