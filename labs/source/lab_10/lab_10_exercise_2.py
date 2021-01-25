# Δημιουργία συνάρτησης square
def square(number):
    # Πολλαπλασιάσουμε κάθε φορά το number
    number *= number
    # Επιστρέφει το number
    return number


# Ζητάμε από το χρήστη να δώσει αριθμό και το μετατρέπουμε σε ακέραιο
num = int(input("Δώσε αριθμό: ").strip())

# Αρχικοποίηση μεταβλητής
athroisma = 0

for i in range(1, num + 1):
    # Καλούμε τη συνάρτηση square
    number = square(i)
    athroisma += number

# Εκτύπωση του αθροίσματος
print(athroisma)
