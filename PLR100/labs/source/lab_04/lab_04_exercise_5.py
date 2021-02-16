# Αρχικοποίηση μεταβλητών
athroisma = 0

# Διαβάζουμε από το χρήστη έναν αριθμό και το μετατρέπουμε σε ακέραιο
number = int(input("Δώσε έναν αριθμό: "))

while number:
    # Παίρνουμε το τελευταίο ψηφίο του αριθμού
    telPshfio = number % 10
    # Παίρνουμε τον αριθμό που απομένει (εκτός του τελευταίου ψηφίου)
    number //= 10
    # Προσθέτουμε κάθε φορά στο athroisma το τελευταίο ψηφίο του αριθμού
    athroisma += telPshfio

# Eκτύπωση αποτελέσματος
print("Το άθροισμα των ψηφίων είναι %d." % athroisma)