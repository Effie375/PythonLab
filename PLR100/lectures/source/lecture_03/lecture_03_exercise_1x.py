# Ζητάμε από το χρήστη έναν αριθμό και το μετατρέπουμε σε πραγματικό
number1 = float(input("Δώσε έναν αριθμό: ").strip())

# Ζητάμε από το χρήστη έναν αριθμό και το μετατρέπουμε σε πραγματικό
number2 = float(input("Δώσε έναν αριθμό: ").strip())

# Ζητάμε από το χρήστη έναν αριθμό και το μετατρέπουμε σε πραγματικό
number3 = float(input("Δώσε έναν αριθμό: ").strip())

# Υπολογίζουμε το άθροισμα των αριθμών αυτών
sum = number1 + number2 + number3

# Εάν το άθροισμα είναι μεγαλύτερο από 100
if sum > 100:
    # Υπολογίζουμε το γινόμενο των δύο πρώτων αριθμών
    ginomeno = number1 * number2
    # Εκτύπωση του γινομένου
    print(f"Το γινόμενο ισούται με {ginomeno:.2f}.")
# Αλλιώς στην περίπτωση που το άθροισμα είναι μικρότερο από το 100
else:
    # Υπολογίζουμε διαφοράς των δύο τελευταίων αριθμών
    diafora = number2 - number3
    # Εκτύπωση της διαφοράς των αριθμών σε απόλυτη τιμή
    print(f"Η διαφορά των αριθμών σε απόλυτη τιμή είναι {abs(diafora)}.")