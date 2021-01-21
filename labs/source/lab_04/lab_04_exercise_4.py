# Αρχικοποίηση μεταβλητών
flag = False
ginomeno = 0
number = 1

# Όσο ο αριθμός είναι διάφορος του μηδενός
while number != 0:
    # Ζητάμε από το χρήστη να δώσει έναν αριθμό
    number = input("Δώσε αριθμό (int): ").strip()
    # Κάνουμε έλεγχο ορθότητας
    while not number.isdigit():
        # Ζητάμε από το χρήστη να δώσει σωστά τον αριθμό
        number = input("Δώσε σωστά ακέραιο αριθμό: ").strip()
    # Μετατρέπουμε τον αριθμό σε ακέραιο
    number = int(number)
    # Μόνο τη πρώτη φορά είναι η συνθήκη true
    if (flag is False):
        # εάν ο αριθμός είναι διάφορος του μηδενός
        if number != 0:
            ginomeno = 1
        # Αλλαγή του flag από False σε True
        flag = True
    # εάν ο αριθμός είναι διάφορος του μηδενός
    if number != 0:
        # Υπολογίζει κάθε φορά το γίνομενο
        ginomeno *= number

# Eκτύπωση αποτελέσματος
print(f"Γινόμενο: {ginomeno}")
