# Αρχικοποίηση μεταβλητών
i = 0
synolo = 0

while i < 10:
    number = input("Δώσε αριθμό: ")
    # Έλεγχος ορθότητας
    while not number.isdigit():
        number = input("Είπα δώσε αριθμό: ")
    number = int(number)
    synolo = synolo + number
    i = i + 1

# Εκτύπωση αποτελέσματος
print("Το σύνολο είναι:", synolo)
