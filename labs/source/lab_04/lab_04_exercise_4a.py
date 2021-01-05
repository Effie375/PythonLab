# Αρχικοποίηση μεταβλητών
flag = False
ginomeno = 0
number = 1

while number != 0:
    # Διάβασμα από τον χρήστη
    number = input("Δώσε αριθμό: ").strip()
    # Έλεγχος ορθότητας
    while not number.isdigit():
        number = input("Δώσε σωστά αριθμό: ").strip()
    # Μετατροπή από str σε int
    number = int(number)
    if (flag is False):
        if number != 0:
            ginomeno = 1
        flag = True
    if number != 0:
        ginomeno *= number

# Eκτύπωση αποτελέσματος
print(f"Γινόμενο: {ginomeno}")
